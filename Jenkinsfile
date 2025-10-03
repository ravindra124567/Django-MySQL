pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/ravindra124567/Django-MySQL.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Migrations') {
            steps {
                sh '. venv/bin/activate && python manage.py migrate'
            }
        }

        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && python manage.py test'
            }
        }

        stage('Build Success') {
            steps {
                echo "Django + MySQL Pipeline executed successfully ✅"
            }
        }
    }
}
