5. Configure CI/CD Pipeline: Jenkins + Ansible + Docker (All from Scratch) 
Note: No DockerHub/ready images 
● Implement a CI/CD pipeline that pulls code, builds Docker image, and runs 
Ansible for remote deployment on a Linux server or VM. 
-----------------------------------------------------------------------------------------
Complete CI/CD Pipeline with Jenkins, Docker, and Kubernetes - Built from Scratch! 🔥

📋 Table of Contents

🎯 Project Overview
✨ Features
🏗️ Architecture
🛠️ Tech Stack
📦 Prerequisites
🚀 Quick Start
📁 Project Structure
⚙️ Configuration
🔄 Pipeline Stages
🐳 Docker Setup
☸️ Kubernetes Deployment
📊 Monitoring
🧪 Testing
🔧 Troubleshooting
🤝 Contributing
📚 Learning Resources
📄 License

🎯 Project Overview
This project demonstrates a complete CI/CD pipeline built from scratch using Jenkins, Docker, and Kubernetes. It automates the entire software delivery process from code commit to production deployment with zero-downtime rolling updates.
🎪 What Makes This Special?

🏗️ Custom Jenkins Setup - No pre-built images, everything from scratch
🐳 Self-hosted Docker Registry - Complete control over your container images
☸️ Kubernetes Integration - Production-ready deployments with health checks
🔄 Automated CI/CD - From code to production in minutes
💻 Windows Compatible - Runs perfectly on Windows with Docker Desktop

✨ Features
FeatureDescriptionStatus🔨 Custom Jenkins BuildBuilt from official Jenkins LTS with Docker CLI✅🐳 Docker RegistrySelf-hosted registry on port 5000✅🚀 Automated Pipeline6-stage pipeline with error handling✅☸️ K8s DeploymentRolling updates with 3 replicas✅❤️ Health ChecksLiveness and readiness probes✅📊 Resource ManagementCPU/Memory limits and requests✅🔒 SecurityNon-root containers and secrets✅📱 Sample AppNode.js Express application✅
🏗️ Architecture
mermaidgraph TB
    A[👨‍💻 Developer] -->|git push| B[📦 GitHub Repository]
    B --> C[🔨 Jenkins Pipeline]
    C --> D[🐳 Docker Build]
    D --> E[🧪 Run Tests]
    E --> F[📤 Push to Registry]
    F --> G[☸️ Deploy to K8s]
    G --> H[✅ Health Check]
    H --> I[🌐 Application Live]
    
    J[🗄️ Docker Registry] --> F
    K[📊 Monitoring] --> I
🛠️ Tech Stack
🧰 Core Technologies

Jenkins - CI/CD Orchestration
Docker - Containerization
Kubernetes - Container Orchestration
Node.js - Sample Application


🔧 Tools & Utilities

Docker Compose - Multi-container orchestration
kubectl - Kubernetes CLI
Git - Version control
Express.js - Web framework
YAML - Configuration files

📦 Prerequisites
🖥️ System Requirements



🛠️ Required Software
Essential tools
✅ Docker Desktop (with Kubernetes enabled)
✅ Git for Windows
✅  5.1+
✅ VS Code or preferred editor

# Optional but recommended
✅ Kubernetes Lens (K8s GUI)
✅ Postman (API testing)
✅ Windows Terminal
🚀 Quick Start
1️⃣ Clone Repository
powershellgit clone https://github.com/anuragdey123/K8s-Manual-CI-CD-Setup7.git
cd K8s-Manual-CI-CD-Setup7
2️⃣ Create Project Structure
powershell# Navigate to your workspace
cd C:\Users\shiva

# Create main project folder
mkdir jenkins-docker-project
cd jenkins-docker-project

# Create folder structure
mkdir jenkins-setup, docker-registry, sample-app, k8s-manifests
3️⃣ Start Services
 Start Docker Registry
cd docker-registry
docker-compose up -d

# Start Jenkins
cd ..\jenkins-setup
docker-compose up -d
4️⃣ Access Jenkins
 Get Jenkins admin password
docker exec jenkins-master cat /var/jenkins_home/secrets/initialAdminPassword

# Open browser
start http://localhost:8080
5️⃣ Verify Setup
 Check all services
docker ps
kubectl get nodes
curl http://localhost:5000/v2/_catalog
📁 Project Structure
jenkins-docker-project/
├── 🔨 jenkins-setup/
│   ├── jenkins-data/           # Jenkins home directory
│   ├── jenkins-logs/           # Jenkins logs
│   ├── docker-compose.yml      # Jenkins service definition
│   ├── Dockerfile              # Custom Jenkins image
│   └── plugins.txt             # Required Jenkins plugins
├── 🐳 docker-registry/
│   ├── registry-data/          # Registry storage
│   ├── docker-compose.yml      # Registry service definition
│   └── config.yml              # Registry configuration
├── 📱 sample-app/
│   ├── src/
│   │   ├── app.js              # Node.js application
│   │   └── package.json        # NPM dependencies
│   ├── Dockerfile              # Application container
│   └── Jenkinsfile             # Pipeline definition
└── ☸️ k8s-manifests/
    ├── deployments/
    │   └── app-deployment.yml   # Kubernetes deployment
    └── services/
        └── app-service.yml      # Kubernetes service
⚙️ Configuration
🔨 Jenkins Configuration
Required Plugins
textworkflow-aggregator:latest      # Pipeline support
docker-workflow:latest          # Docker integration
kubernetes:latest               # K8s integration
git:latest                     # Git SCM
pipeline-stage-view:latest     # Pipeline visualization
blueocean:latest               # Modern UI
credentials:latest             # Credential management
credentials-binding:latest     # Credential binding
Environment Variables
groovyenvironment {
    DOCKER_REGISTRY = 'localhost:5000'
    IMAGE_NAME = 'sample-app'
    IMAGE_TAG = "${BUILD_NUMBER}"
    KUBECONFIG = '/var/jenkins_home/.kube/config'
}
🐳 Docker Registry Setup
The registry runs on localhost:5000 with persistent storage:
yaml# docker-registry/docker-compose.yml
version: '3.8'
services:
  registry:
    image: registry:2
    ports:
      - "5000:5000"
    volumes:
      - ./registry-data:/var/lib/registry
☸️ Kubernetes Configuration
Deployment Features

Replicas: 3 instances for high availability
Rolling Updates: Zero-downtime deployments
Health Checks: Liveness and readiness probes
Resource Limits: CPU and memory constraints
Security: Non-root user execution

Service Configuration

Type: NodePort
External Port: 30080
Internal Port: 3000
Load Balancing: Automatic

🔄 Pipeline Stages
📊 Complete Pipeline Flow
mermaidgraph LR
    A[1️⃣ Checkout] --> B[2️⃣ Build]
    B --> C[3️⃣ Test]
    C --> D[4️⃣ Push]
    D --> E[5️⃣ Deploy]
    E --> F[6️⃣ Verify]
StageDescriptionDurationKey Actions🔄 CheckoutSource code retrieval~10sGit clone, branch checkout🔨 BuildDocker image creation~2-5minDockerfile build, tagging🧪 TestAutomated testing~30sUnit tests, container tests📤 PushRegistry deployment~1-2minImage push, registry update🚀 DeployKubernetes rollout~1-3minK8s deployment, service update✅ VerifyHealth validation~30sPod status, service check
🔧 Pipeline Configuration
groovypipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}")
                }
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh "kubectl apply -f k8s-manifests/"
                }
            }
        }
    }
}
🐳 Docker Setup
📱 Sample Application Container
Multi-stage optimized Dockerfile:
dockerfileFROM node:18-alpine

WORKDIR /app

# Copy package files
 src/package*.json ./

# Install dependencies
RUN npm install --production

# Copy source code
COPY src/ .

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
   curl -f http://localhost:3000/health || exit 1

# Security: Use non-root user
USER node

CMD ["npm", "start"]
🔒 Security Features

Non-root execution - Container runs as node user
Minimal base image - Alpine Linux for smaller attack surface
Health checks - Container self-monitoring
Read-only filesystem - Where possible

☸️ Kubernetes Deployment
🚀 Deployment Strategy
Rolling Update Configuration:
yamlspec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 1
📊 Resource Management
yamlresources:
  requests:
    memory: "128Mi"
    cpu: "100m"
  limits:
    memory: "256Mi"
    cpu: "200m"
❤️ Health Checks
yamllivenessProbe:
  httpGet:
    path: /health
    port: 3000
  initialDelaySeconds: 30
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /health
    port: 3000
  initialDelaySeconds: 5
  periodSeconds: 5
📊 Monitoring
🔍 Application Monitoring
Built-in endpoints:

Health Check: GET /health
Application: GET /
Metrics: Available for Prometheus integration

📈 Infrastructure Monitoring
 Check Jenkins status
docker logs jenkins-master

# Monitor registry
curl http://localhost:5000/v2/_catalog

# Kubernetes monitoring
kubectl get pods -w
kubectl top pods
kubectl describe deployment sample-app-deployment
🚨 Alerting
Pipeline notifications:

✅ Success: Build completed successfully
❌ Failure: Build failed with error details
⚠️ Warning: Tests passed but with warnings

🧪 Testing
🔬 Automated Tests
Pipeline testing stages:
bash# Unit tests
npm test

# Container health test
docker run --rm ${IMAGE_NAME} npm test

# Integration tests
curl -f http://localhost:3000/health
🎯 Manual Testing
Test application locally
docker run -p 3000:3000 localhost:5000/sample-app:latest

# Test Kubernetes deployment
kubectl port-forward svc/sample-app-service 8080:80
curl http://localhost:8080

# Load testing
for i in {1..100}; do curl http://localhost:30080; done
🔧 Troubleshooting
🚨 Common Issues
IssueSymptomsSolutionJenkins won't startContainer exits immediatelyCheck volume permissions, Docker socketRegistry unreachablePush/pull failsVerify registry is running on port 5000K8s deployment failsPods in pending stateCheck resource availability, image pullHealth checks failPods restart continuouslyVerify application health endpoint
🔍 Debug Commands
powershell# Jenkins debugging
docker logs jenkins-master -f
docker exec -it jenkins-master bash

# Registry debugging
docker logs local-docker-registry
curl -v http://localhost:5000/v2/_catalog

# Kubernetes debugging
kubectl describe pod <pod-name>
kubectl logs -f deployment/sample-app-deployment
kubectl get events --sort-by=.metadata.creationTimestamp
🆘 Recovery Commands
powershell# Restart all services
docker-compose restart

# Clean Docker system
docker system prune -a

# Reset Kubernetes deployment
kubectl delete deployment sample-app-deployment
kubectl delete service sample-app-service
kubectl apply -f k8s-manifests/
🤝 Contributing
We welcome contributions! Here's how you can help:
🎯 Ways to Contribute

🐛 Bug Reports - Found an issue? Let us know!
💡 Feature Requests - Have an idea? Share it!
📖 Documentation - Help improve our docs
🔧 Code Contributions - Submit PRs for fixes/features

📋 Contribution Guidelines

Fork the repository
Create feature branch: git checkout -b feature/amazing-feature
Commit changes: git commit -m 'Add amazing feature'
Push to branch: git push origin feature/amazing-feature
Open Pull Request

🧪 Development Setup
 Clone your fork
git clone https://github.com/your-username/K8s-Manual-CI-CD-Setup7.git
cd K8s-Manual-CI-CD-Setup7

# Create development branch
git checkout -b development

# Start development environment
docker-compose -f docker-compose.dev.yml up -d
📚 Learning Resources
🎓 Educational Content
🔨 Jenkins Resources

Jenkins Official Documentation
Pipeline Syntax Reference
Jenkins Docker Plugin

🐳 Docker Learning

Docker Official Tutorial
Docker Compose Guide
Dockerfile Best Practices

☸️ Kubernetes Resources

Kubernetes Documentation
kubectl Cheat Sheet
K8s Best Practices

🎯 Project Inspiration
This project was developed as part of:

🎓 #LinuxWorldInternship with #VimalDagaSir
🚀 #SummerInternship2025 experience
💡 #RealLearning and #BeyondCollege initiative

🌟 Acknowledgments
Special thanks to:

Vimal Daga Sir for mentorship and guidance
LinuxWorld Community for continuous support
Fellow interns for collaboration and learning

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
MIT License

Copyright (c) 2025 Anurag Dey

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

🎉 Final Notes
🚀 What's Next?
Upcoming features:

📊 Prometheus + Grafana monitoring integration
🔒 SSL/TLS security implementation
🌐 Multi-environment deployments (dev/staging/prod)
🤖 Slack/Teams notification integration
🔄 GitOps with ArgoCD



🌟 Star this Repository
If this project helped you learn something new, please ⭐ star this repository and share it with others!
Happy coding! 🚀💻

Made with ❤️ by Anurag Dey
