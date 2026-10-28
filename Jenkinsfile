pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/tarrsan2024-wq/Library'
            }
        }
        stage('Compile') {
            steps {
                bat 'python app.py'
            }
        }
    }
}