pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/GangadharUppin/python_selenium_git_code.git'
        BRANCH = 'master'
        VENV_DIR = 'venv'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: "${BRANCH}", url: "${REPO_URL}"
            }
        }

        stage('Set Up Python Environment') {
            steps {
                // Install Python and pip if not already installed (optional)
                // Create virtual environment and activate it
                sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    pytest tests/ --maxfail=1 --disable-warnings --tb=short
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
        }
        success {
            echo 'Build and tests successful.'
        }
        failure {
            echo 'Build or tests failed.'
        }
    }
}
