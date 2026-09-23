pipeline {
    agent { label 'windows' } // Ensures it runs on your Windows agent

    stages {
        stage('Checkout') {
            steps {
                // Pulls code from your repository
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
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
