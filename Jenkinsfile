pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                     sh "docker-compose -f docker-compose.yaml up"
                    }
                }
            }
    }
    post {
        always {
            cleanWs()
        }
    }
}