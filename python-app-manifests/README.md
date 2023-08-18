# Deploying Your Dockerized Web Service with Kubernetes

This guide will walk you through the process of deploying your Dockerized web service using Kubernetes. We'll create a Kubernetes Deployment and a Service to expose your web service internally within the Minikube cluster.

## Prerequisites

Before you begin, ensure you have the following:

- Minikube set up on your local machine
- Docker image of your web service

## Deployment Steps
Apply the Deployment manifest:

   ```bash
   kubectl apply -f deployment.yaml
```

Apply the Service manifest:

   ```bash 
   kubectl apply -f service.yaml
```

## Accessing Your Web Service
Once the deployment is successful, you can access your web service within the Minikube cluster using the Service's PodIP:NodePort.

## Cleaning up
```bash
kubectl delete deployment my-python-app
kubectl delete service my-python-service
```

