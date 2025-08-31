pipeline {
    agent {
        /*label 'Ec2-Agent'*/
        label any
    }
    triggers{
        pollSCM('H/30 * * * *')
    }

    environment {
        GITHUB_REPO = "https://github.com/Hafez292/weather-app.git"
        BRANCH = "main"
        CREDENTIALS_ID = "Github-Cred"  // Jenkins credential ID
    }

    stages {
        stage('Git Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: "*/${env.BRANCH}"]],
                    userRemoteConfigs: [[
                        url: "${env.GITHUB_REPO}",
                        credentialsId: "${env.CREDENTIALS_ID}"
                    ]]
                ])
            }
        }
        /*stage('ConnectionTo E2-Agent'){
            steps{
                sh '''
                git --version
                java --version
                docker --version
                '''
            }
        }
       
         stage('Testing-Container') {
            agent {
                docker {
                    image "python:3.12-slim"
                    args '--user root -v ${WORKSPACE}:/app-1 -w /app-1'
                    reuseNode true
                    
                }
            }
            steps {
                sh '''
                    # Install packages
                    pip install --upgrade pip
                    pip install flake8 pytest flask requests pytest-mock requests-mock

                    # Lint testing
                    file="/app-1/python-app/weather.py"
                    sed -i -e 's/[[:blank:]]*$//' -e ':a;/^\\n*$/{$d;N;ba}' "$file"
                    flake8 "$file" --extend-ignore=W292,W391
                    
                    # Unit testing
                    pytest /app-1/python-app/test.py -v
                '''
            }
        }
        */

        stage('Building-Image') {
            steps {
                script {
                    docker.build("python-app", "${WORKSPACE}/python-app/")
                    docker.build("nginx", "${WORKSPACE}/nginx/")
                    docker.build("UI","${WORKSPACE}/frontend")
                }
            }
        }

        stage('Push-Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'DockerHub-Credential', 
                    usernameVariable: 'USER', 
                    passwordVariable: 'PASS'
                )]) {
                    sh '''
                        echo $PASS | docker login -u $USER --password-stdin
                        docker tag python-app mohamedtony/weather-app:backend
                        docker tag UI mohamedtony/weather-app:frontend
                        docker tag nginx mohamedtony/weather-app:loadbalancer
                        
                        docker push mohamedtony/weather-app:backend
                        docker push mohamedtony/weather-app:frontend
                        docker push mohamedtony/weather-app:loadbalancer

                    '''
                }
            }
        }
    }

    post {
        always {
            sh 'docker system prune -f'

        }
    }
}