# GitOps CI/CD Pipeline for Python Application deployment using Jenkins, ArgoCD, and Minikube.
![Technical Diagrams (2)](https://github.com/NavazishS/test/assets/72895399/b765bb31-d997-4249-8df2-4f711ddf61fc)

## Prerequisites

- Jenkins Host (AWS EC2)
- ArgoCD
- Minikube
- Docker
- Git
- Python

You can use a combination of AWS, Minikube, and Python to deploy The Responding Dark Laughter (TRDL) web service as a proof-of-concept (PoC) system. Here's a step-by-step guide on how to achieve this:

1. **Install the necessary Jenkins plugins:**
   - 1.1 All recommended plugins asked during installation
   - 1.2 Install 'docker-pipeline' to run the Jenkins agent as a container on the Jenkins host machine.
   - 1.3 Install 'sonar-scanner' in case you want to use it for analyzing your code.

2. **Create a new Jenkins pipeline:**
   - 2.1 In Jenkins, create a new pipeline job and configure it with the Git repository URL.
   - 2.2 Add a Jenkinsfile to the Git repository to define the pipeline stages.

3. **Define the pipeline stages:**
   - **Stage 1:** Checkout the source code from Git by initiating Jenkins' build using a Docker agent.
   - **Stage 2.a:** Copy your Python code and any required dependencies using a Dockerfile as shown in the repository (link).
   - **Stage 2.b:** Build the Docker image with Dockerfile and run the container in a detached mode, exposing its application to the host IP on port 8081.
   - **Stage 2.c:** Run unit tests with 'curl:<jenkins-host-ip:8081>'
   - **Stage 3:** Run SonarQube analysis to check the code quality (Not configured in the current solution).
   - **Stage 4:** Build and Push the Image to the Docker Hub or JFrog repositories or ACR.
   - **Stage 5:** Run user acceptance tests on the deployed application (Not configured for the current application).
   - **Stage 6:** Updating Python application deployment with the latest tag.
   - **Stage 7:** Promote the application to a Minikube Kubernetes environment using Argo CD.
	
4. **Install Minikube on EC2:**
   - 1. SSH into the EC2 instance and install Minikube.
   - 2. Start Minikube using the suitable driver.

5. **Set up Argo CD:**
   - 5.1 Install Argo CD on the Kubernetes cluster.
   - 5.2 Set up a Git repository for Argo CD to track the changes in the Helm charts and Kubernetes manifests.

6. **Configure Jenkins pipeline to integrate with Argo CD:**
   - 6.1 Add the Argo CD API token to Jenkins credentials.
   - 6.2 Update the Jenkins pipeline to include the Argo CD deployment stage.

7. **Run the Jenkins pipeline:**
   - 7.1 Trigger the Jenkins pipeline to start the CI/CD process for the Java application.
   - 7.2 Monitor the pipeline stages and fix any issues that arise.


