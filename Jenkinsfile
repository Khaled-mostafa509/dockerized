pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                echo 'Application is updated successfully..'
                git branch: 'main', credentialsId: 'jenkins-doc-git', url: 'https://github.com/Khaled-mostafa509/dockerized.git'
                sh 'docker build . -t jenkins_nodejs_example:$BUILD_TAG'
            }
            post{
                succsess {
                    sh "docker image ls"
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
