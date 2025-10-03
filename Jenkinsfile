pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/ravindra124567/Django-MySQL.git'
            }
        }

        stage('System Dependencies') {
            steps {
                sh '''
                    sudo apt-get update -y
                    sudo apt-get install -y pkg-config libmysqlclient-dev build-essential python3.12-dev python3.12-venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    # Clean old venv if exists
                    rm -rf venv
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip setuptools wheel
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Migrations') {
            steps {
                sh '''
                    . venv/bin/activate
                    python manage.py migrate
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    python manage.py test
                '''
            }
        }

        stage('Build Success') {
            steps {
                echo "✅ Django + MySQL Pipeline executed successfully!"
            }
        }
    }
}

