# 🚀 GitOps CI/CD Pipeline: Visitor Counter App

A complete, production-grade GitOps pipeline demonstrating the deployment of a Stateful application (Flask + Redis) onto a Kubernetes cluster using GitHub Actions and ArgoCD.

## 🏗️ Architecture Overview

This project implements a pure GitOps workflow:
1. **Developer** pushes code to the GitHub repository.
2. **GitHub Actions (CI)** triggers, builds a Docker image, and pushes it to Docker Hub.
3. **GitHub Actions** automatically updates the image tag in the Kubernetes deployment manifest (`app-deployment.yaml`) and commits the change back to the repo.
4. **ArgoCD (CD)** continuously monitors the `k8s/` directory in the repository. It detects the change and automatically synchronizes the Kubernetes cluster with the desired state.

## 🛠️ Tech Stack

* **Application:** Python, Flask
* **Database:** Redis (In-memory datastore)
* **Containerization:** Docker
* **Container Orchestration:** Kubernetes (Minikube)
* **Continuous Integration (CI):** GitHub Actions
* **Continuous Deployment (CD):** ArgoCD

## 📁 Folder Structure

```text
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


 screenShoots
 <img width="1529" height="777" alt="image" src="https://github.com/user-attachments/assets/c91688d8-018c-480e-9d9e-355e80e4acc5" />
<img width="1534" height="776" alt="image" src="https://github.com/user-attachments/assets/e12aa559-856b-428a-b778-5647a3760225" />

