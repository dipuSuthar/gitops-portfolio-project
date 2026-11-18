🚀 GitOps CI/CD Pipeline: Visitor Counter App

A complete, production-grade GitOps pipeline demonstrating the deployment of a Stateful application (Flask + Redis) onto a Kubernetes cluster using GitHub Actions and ArgoCD.

📸 Screenshots

🏗️ Architecture Overview

This project implements a pure GitOps workflow:

Developer pushes code to the GitHub repository.

GitHub Actions (CI) triggers, builds a Docker image, and pushes it to Docker Hub.

GitHub Actions automatically updates the image tag in the Kubernetes deployment manifest (app-deployment.yaml) and commits the change back to the repo.

ArgoCD (CD) continuously monitors the k8s/ directory in the repository. It detects the change and automatically synchronizes the Kubernetes cluster with the desired state.

🛠️ Tech Stack

Application: Python, Flask

Database: Redis (In-memory datastore)

Containerization: Docker

Container Orchestration: Kubernetes (Minikube)

Continuous Integration (CI): GitHub Actions

Continuous Deployment (CD): ArgoCD

📁 Folder Structure

gitops-portfolio-project/
│
├── .github/workflows/
│   └── ci.yaml               # GitHub Actions CI pipeline
│
├── app/                      # Application Source Code
│   ├── app.py                # Flask application with health probes
│   ├── requirements.txt      # Python dependencies
│   └── Dockerfile            # Production-grade, non-root Dockerfile
│
└── k8s/                      # Kubernetes Manifests (Watched by ArgoCD)
    ├── redis.yaml            # Redis Deployment & Service
    ├── app-deployment.yaml   # Flask App Deployment (Auto-updated by CI)
    └── app-service.yaml      # Flask App NodePort Service


✨ Key Features Implemented

Separation of Concerns: Application code and Kubernetes manifests are cleanly separated.

Stateful Deployment: Uses Redis to maintain state (visitor count) across pod restarts.

Zero-Downtime Updates: ArgoCD ensures smooth rolling updates without manual intervention.

Health Probes: Liveness and Readiness probes configured in Kubernetes for high availability.

Security: Non-root user implementation inside the Dockerfile.

🚀 How to Run Locally

1. Prerequisites

Docker Desktop

Minikube & kubectl

GitHub Account & Docker Hub Account

2. Infrastructure Setup

Start the local Kubernetes cluster and install ArgoCD:

minikube start
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml


3. Deploy via ArgoCD

Port-forward the ArgoCD UI:

kubectl port-forward svc/argocd-server -n argocd 8080:443


Log into ArgoCD UI (https://localhost:8080).

Create a New App pointing to this GitHub repository's k8s folder.

Click Sync to deploy the application and database.

4. Access the Application

Once the deployment is healthy in ArgoCD, access the app:

minikube service gitops-service


Developed by a passionate DevOps Engineer - Showcasing Modern DevOps Practices.