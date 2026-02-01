# Commands to Check Local Kubernetes Deployment

Here's a sequence of commands to showcase your working Kubernetes deployment:

## 1. Docker Status
```bash
# Show Docker is running
docker ps
# Look for the minikube container in the output to confirm Docker is running.
```
## 2. Minikube Status

```bash
# Check Minikube status
minikube status
# Show that the cluster is running (host, kubelet, apiserver all showing as Running).
```
## 3. Helm

```bash
# Show Helm release
helm list
# Demonstrate that your todo-app release is deployed and running.
```
## 4. Kubernetes Resources

```bash
# Show running pods
kubectl get pods
# Show services
kubectl get services

# Show deployments
kubectl get deployments
# Highlight that both frontend and backend pods are running (1/1 ready).
```

## 5. Access Application

```bash
# Get frontend service URL
minikube service todo-app-todo-chatbot-frontend --url

# Get backend service URL
minikube service todo-app-todo-chatbot-backend --url
# Show the accessible URLs for both services.
```

## 6. Port Forwarding

```bash
# Terminal 1: Port forward frontend
kubectl port-forward svc/todo-app-todo-chatbot-frontend 3000:3000

# Terminal 2: Port forward backend (in a separate terminal)
kubectl port-forward svc/todo-app-todo-chatbot-backend 8000:8000
# Show how to access the application locally via port forwarding.
```

## Additional Commands for Smooth Demo:

```bash
# Quick check of cluster info
kubectl cluster-info

# Check logs of frontend pod (if needed)
kubectl logs -l app=frontend

# Check logs of backend pod (if needed)
kubectl logs -l app=backend

# To see live logs with DB and API interactions:
kubectl logs -l app=backend -f
```