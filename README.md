# 🌤️ Weather Dashboard

A containerized weather application that provides real-time weather information for any city worldwide. Built with a modern microservices architecture using Docker containers.

![Weather Dashboard](https://img.shields.io/badge/Version-1.0.0-brightgreen)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Python](https://img.shields.io/badge/Python-3.9%2B-yellow)
![Flask](https://img.shields.io/badge/Flask-API%20Backend-lightgrey)
![Nginx](https://img.shields.io/badge/Nginx-Reverse%20Proxy-green)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-orange)

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Technologies Used](#-technologies-used)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
- [CI/CD Pipeline](#-cicd-pipeline)
- [Usage](#-usage)
- [API Reference](#-api-reference)
- [Project Structure](#-project-structure)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)

## ✨ Features

- 🔍 Search weather by city name
- 🌡️ Display temperature, humidity, and wind conditions
- 🎨 Responsive and modern UI
- 🐳 Containerized with Docker
- 🔄 Reverse proxy with Nginx
- 📱 Mobile-friendly design
- ⚡ Fast and lightweight
- 🔁 CI/CD pipeline with Jenkins

## 🏗️ Architecture

The application follows a microservices architecture with three main components:
```
Client Browser → Nginx (Reverse Proxy) → Frontend Container → Backend Container → WeatherAPI
```

### Component Details:

1. **Frontend**: Static HTML/CSS/JS served by Apache HTTP Server
2. **Backend**: Flask API that fetches data from WeatherAPI.com
3. **Nginx**: Reverse proxy that routes requests and handles SSL termination

## 🛠️ Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Backend**: Python 3.9, Flask, Requests library
- **Web Server**: Nginx, Apache HTTP Server
- **Containerization**: Docker, Docker Compose
- **API**: WeatherAPI.com
- **CI/CD Pipeline**: Jenkins
- **Cloud**:EC2

## 📋 Prerequisites

Before running this application, ensure you have the following installed:

- Docker Engine (version 20.10.0+)
- Docker Compose (version 2.0.0+)
- Git

For CI/CD pipeline:
- Jenkins server with EC2 agent
- DockerHub account

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Hafez292/Microservice-weather-app
cd weather-app
```

### 2. Set Up Environment Variables

Create a `.env` file in the root directory:

```bash
# WeatherAPI.com API Key
WEATHER_API_KEY=your_api_key_here

# Optional: Change port mapping if needed
NGINX_HOST_PORT=8000
```

You can get a free API key from [WeatherAPI.com](https://www.weatherapi.com/)

### 3. Build and Run the Application

```bash
docker-compose up --build -d
```

### 4. Access the Application

Open your web browser and navigate to:
- **Main Application**: http://localhost:8000
- **API Health Check**: http://localhost:8000/api/health

🔁 CI/CD Pipeline
This project includes a Jenkins pipeline for continuous integration and deployment:

  Pipeline Stages:
  Checkout: Pull the latest code from the repository
  
  Test Backend API: Run tests inside the backend container
  
  Build Docker Images: Build Docker images for all services
  
  Push to DockerHub: Push images to DockerHub registry
  
  Deploy: Deploy the updated containers to the target environment
  
  Setup Instructions:
  Jenkins Configuration:
  
  Install required plugins: Docker Pipeline, Git, Credentials Binding
  
  Set up credentials in Jenkins:
  
  dockerhub-credentials (Username and password for DockerHub)
  
  weather-api-key (Secret text for WeatherAPI key)
  
  EC2 Agent Setup:
  
  Ensure Docker and Docker Compose are installed on the agent
  
  Configure the agent with the label 'ec2-agent'
  
  Create Pipeline:
  
  Create a new Pipeline job in Jenkins
  
  Set definition to "Pipeline script from SCM"
  
  Configure your repository URL
  
  Set script path to "Jenkinsfile"

## 🎯 Usage

1. Open the application in your web browser
2. Enter a city name in the search box
3. Click "Search" or press Enter
4. View the current weather conditions for that city

### Example Searches:
- London
- New York
 
## 🔌 API Reference

### Get Weather by City

```
GET /api/weather?city={city_name}
```

#### Parameters:
- `city` (required): Name of the city to get weather for

#### Response:
```json
{
  "city": "London",
  "country": "United Kingdom",
  "temperature": "15°C",
  "feels_like": "14°C",
  "wind_speed": "12 km/h",
  "wind_direction": "SW",
  "humidity": "78%",
  "condition": "Partly cloudy",
  "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
  "last_updated": "2023-08-31 12:00"
}
```

### Health Check

```
GET /api/health
```

#### Response:
```json
{
  "status": "healthy",
  "service": "weather-api"
}
```

## 📁 Project Structure

```
weather-app/
├── docker-compose.yml          # Docker container orchestration
├── .env                        # Environment variables                    
├── Jenkinsfile                 # CI/CD (Testing/Build/Push) Images To DokerHub
├── nginx/
│   ├── Dockerfile              # Nginx container configuration
│   └── nginx.conf              # Nginx reverse proxy settings
├── backend/
│   ├── Dockerfile              # Python/Flask container configuration
│   ├── requirements.txt        # Python dependencies
│   └── weather_api.py          # Flask API implementation
└── frontend/
    ├── Dockerfile              # Apache web server configuration
    ├── index.html              # Main HTML file
    ├── style.css               # Stylesheet
    └── script.js               # Frontend JavaScript logic
```

## 🐛 Troubleshooting

### Common Issues:

1. **Port already in use error**:
   ```bash
   # Change the port in docker-compose.yml or stop the conflicting service
   sudo lsof -i :80
   sudo systemctl stop apache2
   ```

2. **API key not working**:
   - Ensure you have a valid WeatherAPI.com key
   - Check that the key is correctly set in the .env file

3. **Container build failures**:
   ```bash
   # Rebuild with no cache
   docker-compose build --no-cache
   ```

4. **Check container logs**:
   ```bash
   docker-compose logs nginx
   docker-compose logs backend
   docker-compose logs frontend
   ```

### Useful Docker Commands:

```bash
# Start containers in detached mode
docker-compose up -d

# Stop containers
docker-compose down

# View running containers
docker ps

# View container logs
docker-compose logs [service_name]

# Rebuild specific service
docker-compose build [service_name]
```

## 📝 License

This project is licensed Hafez292@github .

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📞 Support

If you have any questions or need support,  contact With Me.

---

