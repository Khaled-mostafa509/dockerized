pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                echo 'Application is updated successfully..'
                git branch: 'main', credentialsId: 'jenkins-doc-git', url: 'https://github.com/Khaled-mostafa509/dockerized.git'
                sh 'docker build . -t khaledrepo'
                sh 'docker compose up'
            }
            post{
                success {
                    sh "docker ps"
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
