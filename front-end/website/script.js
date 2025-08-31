document.addEventListener('DOMContentLoaded', function() {
    const cityInput = document.getElementById('city-input');
    const searchBtn = document.getElementById('search-btn');
    const weatherInfo = document.getElementById('weather-info');
    const errorMessage = document.getElementById('error-message');
    const loading = document.getElementById('loading');
    const recentSearches = document.getElementById('recent-searches');
    const recentList = document.getElementById('recent-list');
    
    // API endpoint
    const API_URL = 'api/weather';
    
    // Load recent searches from localStorage
    let recentCities = JSON.parse(localStorage.getItem('recentCities')) || [];
    updateRecentCities();
    
    searchBtn.addEventListener('click', getWeather);
    cityInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            getWeather();
        }
    });
    
    function getWeather() {
        const city = cityInput.value.trim();
        
        if (!city) {
            showError('Please enter a city name');
            return;
        }
        
        // Show loading, hide previous results and errors
        loading.style.display = 'flex';
        weatherInfo.style.display = 'none';
        errorMessage.style.display = 'none';
        
        // Make API request
        fetch(`${API_URL}?city=${encodeURIComponent(city)}`)
            .then(response => {
                if (!response.ok) {
                    return response.json().then(err => { throw err; });
                }
                return response.json();
            })
            .then(data => {
                // Add to recent searches
                addToRecentCities(city);
                displayWeather(data);
            })
            .catch(error => {
                const errorMsg = error.error || 'Failed to fetch weather data. Please check your connection and try again.';
                showError(errorMsg);
            })
            .finally(() => {
                loading.style.display = 'none';
            });
    }
    
    function displayWeather(data) {
        document.getElementById('city-name').textContent = data.city;
        document.getElementById('country').textContent = data.country;
        document.getElementById('temperature').textContent = data.temperature;
        document.getElementById('feels-like').textContent = `Feels like ${data.feels_like}`;
        document.getElementById('weather-condition').textContent = data.condition;
        document.getElementById('weather-icon').src = data.icon.startsWith('//') ? `https:${data.icon}` : data.icon;
        document.getElementById('wind-speed').textContent = data.wind_speed;
        document.getElementById('wind-direction').textContent = data.wind_direction;
        document.getElementById('humidity').textContent = data.humidity;
        document.getElementById('last-updated').textContent = `Last updated: ${data.last_updated}`;
        
        weatherInfo.style.display = 'block';
        errorMessage.style.display = 'none';
    }
    
    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.style.display = 'block';
        weatherInfo.style.display = 'none';
    }
    
    function addToRecentCities(city) {
        // Remove if already exists
        recentCities = recentCities.filter(c => c.toLowerCase() !== city.toLowerCase());
        
        // Add to beginning of array
        recentCities.unshift(city);
        
        // Keep only 5 recent cities
        if (recentCities.length > 5) {
            recentCities.pop();
        }
        
        // Save to localStorage
        localStorage.setItem('recentCities', JSON.stringify(recentCities));
        
        // Update UI
        updateRecentCities();
    }
    
    function updateRecentCities() {
        if (recentCities.length > 0) {
            recentSearches.style.display = 'block';
            recentList.innerHTML = '';
            
            recentCities.forEach(city => {
                const cityElement = document.createElement('div');
                cityElement.className = 'recent-city';
                cityElement.textContent = city;
                cityElement.addEventListener('click', () => {
                    cityInput.value = city;
                    getWeather();
                });
                
                recentList.appendChild(cityElement);
            });
        } else {
            recentSearches.style.display = 'none';
        }
    }
});