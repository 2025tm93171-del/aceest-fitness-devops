pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aceest-fitness:latest .'
            }
        }
    }

    post {
        always {
            echo 'ACEest Fitness CI pipeline finished.'
        }
    }
}