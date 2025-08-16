pipeline {
    agent { label 'ubuntu' }

    environment {
        IMAGE_NAME = "python-selenium-test"
    }


    stages {
        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/GangadharUppin/python_selenium_git_code.git', branch: 'master'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME} -f integrate_ci_cd/Dockerfile .
                '''
            }
        }

        stage('Run Tests Using Docker (on EC2 host)') {
            steps {
                sh '''
                     #!/bin/bash
                     docker run --rm -v /dev/shm:/dev/shm ${IMAGE_NAME} pytest tests -vm sanity
                '''
            }
        }
    }


    post {
        always {
            //archiveArtifacts artifacts: 'screenshots/*.png', allowEmptyArchive: true
            emailext (
                subject: "Test Email is as following  - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "<p>This is a test email from Jenkinsfile</p>",
                mimeType: 'text/html',
                to: "akhilagangadharuppin@gmail.com",
                attachLog: true
            )
        }
    }
}




