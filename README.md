# Automation Testing for Frontend and Backend sample scripts

## Requirements to be installed :
- Minikube or similar for Kubernetes
- Python3 with `requests` module
- Docker images for both frontend and backend services

## Setup Instructions :

1. Start Minikube: `minikube start`
2. Bash script for Applying Kubernetes Deployment:
   ```bash
   kubectl apply -f backend-deployment.yaml
   kubectl apply -f frontend-deployment.yaml
   ```
3. Access the frontend service using: `minikube service frontend-service`
4. Run the automated test script:
   ```bash
   python test_integration.py
   ```

## Automated Test Script: 
The script will check that the frontend correctly displays the message fetched from the backend.
