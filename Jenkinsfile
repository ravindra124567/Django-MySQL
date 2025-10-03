pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
        DB_NAME = "mydb"
        DB_USER = "myuser"
        DB_PASS = "mypassword"
        DB_ROOT_PASS = "root"
        DB_HOST = "127.0.0.1"
        DB_PORT = "3306"
    }

    stages {

        stage('Checkout SCM') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/ravindra124567/Django-MySQL.git',
                    credentialsId: 'GITS_CREDENTIAL'
            }
        }

        stage('Start MySQL Docker') {
            steps {
                sh '''
                    # Remove old container if exists
                    docker rm -f mysql-server || true
                    # Start new MySQL container
                    docker run -d --name mysql-server \
                        -e MYSQL_ROOT_PASSWORD=$DB_ROOT_PASS \
                        -e MYSQL_DATABASE=$DB_NAME \
                        -e MYSQL_USER=$DB_USER \
                        -e MYSQL_PASSWORD=$DB_PASS \
                        -p $DB_PORT:3306 mysql:8
                    # Wait for MySQL to initialize
                    sleep 20
                '''
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Configure Django DB Settings') {
            steps {
                sh '''
                    # Update settings.py dynamically for CI environment
                    sed -i "s/'HOST': '.*'/'HOST': '$DB_HOST'/g" project/settings.py
                    sed -i "s/'PORT': '.*'/'PORT': '$DB_PORT'/g" project/settings.py
                    sed -i "s/'USER': '.*'/'USER': '$DB_USER'/g" project/settings.py
                    sed -i "s/'PASSWORD': '.*'/'PASSWORD': '$DB_PASS'/g" project/settings.py
                    sed -i "s/'NAME': '.*'/'NAME': '$DB_NAME'/g" project/settings.py
                '''
            }
        }

        stage('Run Migrations') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    python manage.py migrate
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    python manage.py test
                '''
            }
        }

        stage('Build Success') {
            steps {
                echo 'Pipeline executed successfully!'
            }
        }
    }

    post {
        always {
            sh 'docker rm -f mysql-server || true'  // Clean up container
        }
        failure {
            echo 'Pipeline failed!'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
    }
}
