pipeline {
    agent any // Automatically picks your available agent without throwing label errors

    stages {
        stage('Checkout') {
            steps {
                // Pulls the latest code from your GitHub repository
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Creates a virtual environment and installs pytest on Windows
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Runs the pytest suite and generates a results report
                bat '''
                call venv\\Scripts\\activate
                pytest test_app.py --junitxml=results.xml
                '''
            }
        }
    }

    post {
        success {
            echo '🎉 Jenkins Build Status: SUCCESS! All tests passed flawlessly.'
        }
        failure {
            echo '🚨 Jenkins Build Status: FAILURE! One or more unit tests failed.'
        }
    }
}
