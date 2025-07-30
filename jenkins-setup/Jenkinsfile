pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git ' https://github.com/anuragdey123/K8s-Manual-CI-CD-Setup7.git' 
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t flaskapp:latest ./app'
                }
            }
        }

        stage('Run Ansible Deployment') {
            steps {
                sh 'ansible-playbook -i ansible-setup/inventory ansible-setup/deploy.yaml'
            }
        }
    }
}
