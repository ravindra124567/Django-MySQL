pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = 'python3'
        VENV_PATH = "${WORKSPACE}/venv"
        MYSQL_CONTAINER = 'jenkins-mysql-test'
        MYSQL_ROOT_PASSWORD = 'root'
        MYSQL_DATABASE = 'mydb'
        MYSQL_USER = 'myuser'
        MYSQL_PASSWORD = 'mypassword'
        MYSQL_PORT = '3307'  // Changed to avoid conflicts
    }
    
    stages {
        stage('Checkout SCM') {
            steps {
                git branch: 'main',
                    credentialsId: 'GITS_CREDENTIAL',
                    url: 'https://github.com/ravindra124567/Django-MySQL.git'
            }
        }
        
        stage('Start MySQL Docker') {
            steps {
                sh """
                    # Remove any existing container
                    docker rm -f ${MYSQL_CONTAINER} || true
                    
                    # Start MySQL container
                    docker run -d \
                        --name ${MYSQL_CONTAINER} \
                        -e MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} \
                        -e MYSQL_DATABASE=${MYSQL_DATABASE} \
                        -e MYSQL_USER=${MYSQL_USER} \
                        -e MYSQL_PASSWORD=${MYSQL_PASSWORD} \
                        -p ${MYSQL_PORT}:3306 \
                        mysql:8
                    
                    # Wait for MySQL to be ready
                    echo "Waiting for MySQL to initialize..."
                    sleep 30
                    
                    # Test MySQL connection
                    for i in {1..30}; do
                        if docker exec ${MYSQL_CONTAINER} mysqladmin ping -h localhost --silent; then
                            echo "MySQL is ready!"
                            break
                        fi
                        echo "Waiting for MySQL... (\$i/30)"
                        sleep 2
                    done
                """
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                sh """
                    # Clean old venv if exists
                    rm -rf ${VENV_PATH}
                    
                    # Create new virtual environment
                    ${PYTHON_VERSION} -m venv ${VENV_PATH}
                    
                    # Upgrade pip
                    ${VENV_PATH}/bin/pip install --upgrade pip setuptools wheel
                """
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh """
                    ${VENV_PATH}/bin/pip install -r requirements.txt
                """
            }
        }
        
        stage('Configure Django DB Settings') {
            steps {
                sh '''
                    # Update Django settings for MySQL
                    cat > local_settings.py << EOF
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '${MYSQL_DATABASE}',
        'USER': '${MYSQL_USER}',
        'PASSWORD': '${MYSQL_PASSWORD}',
        'HOST': 'localhost',
        'PORT': '${MYSQL_PORT}',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}
EOF
                    cat local_settings.py
                '''
            }
        }
        
        stage('Run Migrations') {
            steps {
                sh """
                    ${VENV_PATH}/bin/python manage.py migrate --noinput
                """
            }
        }
        
        stage('Run Tests') {
            steps {
                sh """
                    ${VENV_PATH}/bin/python manage.py test --noinput
                """
            }
        }
        
        stage('Build Success') {
            steps {
                echo "✅ Django + MySQL Pipeline executed successfully!"
            }
        }
    }
    
    post {
        always {
            sh """
                # Stop and remove MySQL container
                docker rm -f ${MYSQL_CONTAINER} || true
            """
            echo "🧹 Cleaned up MySQL container"
        }
        success {
            echo "🎉 Pipeline completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed. Check the logs above."
        }
    }
}
