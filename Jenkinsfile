pipeline {
       agent any  // use any available Windows agent
    environment {
        REPO_URL = 'https://github.com/GangadharUppin/python_selenium_git_code.git'
        BRANCH = 'master'
        VENV_DIR = 'venv'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo 'clone repo'
                git branch: "${BRANCH}", url: "${REPO_URL}"
            }
        }

        stage('Set Up Python Environment') {
            steps {
                 echo 'setup python environment'
                script {
                    if (isUnix()) {
                        sh '''
                            python3 -m venv ${VENV_DIR}
                            . ${VENV_DIR}/bin/activate
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            python -m venv %VENV_DIR%
                            call %VENV_DIR%\\Scripts\\activate
                            python -m pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            . ${VENV_DIR}/bin/activate
                            pytest tests/ --maxfail=1 --disable-warnings --tb=short
                        '''
                    } else {
                        bat '''
                            call %VENV_DIR%\\Scripts\\activate
                            pytest tests/ --maxfail=1 --disable-warnings --tb=short
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            echo '📧 Attempting to send email...'
            emailext (
                subject: "Simple Email from Jenkins Pipeline",
                body: "Testing post block email sending.",
                to: "akhilagangadharuppin@gmail.com"
            )
        }
    }
}