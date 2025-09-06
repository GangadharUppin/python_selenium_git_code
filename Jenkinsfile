pipeline {
    agent any   // Make sure you have a Windows agent node
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'master', url: 'https://github.com/YourUserName/YourRepo.git'
            }
        }
        stage('Run Test') {
            steps {
                bat """
                cd C:\\Users\\ACER\\Desktop\\Learning\\python_selenium_git_code
                call venv\\Scripts\\activate
                pytest -v -s -m sanity
                """
            }
        }
    }
}
