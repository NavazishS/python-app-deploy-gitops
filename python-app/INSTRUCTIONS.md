This repository demonstrates a GitOps-style CI/CD pipeline for deploying a Python-based application using Jenkins, ArgoCD, and Minikube. The pipeline automates the build, test, and deployment process in a Kubernetes environment.

## Table of Contents

- [Pipeline Stages](#PipelineStages)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Instructions](#Instructions)


## Pipeline Stages

### Source Code Management

1. Configure your Git repository with the Python application source code.
2. Use Jenkins to monitor the repository for changes.

### Build and Test

1. Jenkins initiates a build using a Docker agent.
2. The Python application is built and tested within the Docker container.

### SonarQube Analysis

- The build triggers a SonarQube analysis to ensure code quality and detect issues.

### Docker Image Creation

- Upon successful tests, a custom Docker image is created with the Python application.

### Push Docker Image

- The Docker image is pushed to a Docker registry (e.g., Docker Hub).

### GitOps Deployment

1. ArgoCD watches for changes in the Git repository.
2. When the Docker image changes are updated to the deployment manifest file, ArgoCD deploys the new version to Minikube.

## Getting Started

### Prerequisites

- Jenkins Host (AWS EC2)
- ArgoCD
- Minikube
### Instructions

1. **Clone this repository:**

   ```bash
   git clone https://github.com/NavazishS/python-app-deploy-gitops.git
   cd python-app
2. **Update JenkinsFile:**
 
  - 2.1 Add your actual Jenkins host IP in the below line
    ```bash
    CURL_OUTPUT=$(curl -s http://<Jenkins_Host_IP>:8081)
  - 2.2 Add Dockerhub credentials as

     ```bash
     Type='Username and password', Id='docker-cred', Username=<YOUR_DOCKERHUB_USERNAME>, Password=<YOUR_DOCKERHUB_PASSWORD> 
  - 2.3 Add Github credentials as

     ```yaml
     Type='Secret text', Id='jenkins-github', Secret=<YOUR_GITHUB_PAT_TOKEN_WITH_REQUIRED_ACCESS>
  - 2.4 Update GIT_USER_NAME  with your github username 


3. **Run the Pipeline:**

  - 3.1 Make changes to the source code and push them to the Git repository.
  - 3.2 Observe the pipeline stages running automatically.

Congratulations! Now you can access your web service result with `curl http://<pod-ip-address>:<Nodeport>`
