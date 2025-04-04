# Kubernetes Project Deployment
Working Link : https://67eb7b3602afc75d81781716--golden-sopapillas-bed010.netlify.app/
![Kubernetes Logo](https://upload.wikimedia.org/wikipedia/commons/3/39/Kubernetes_logo_without_workmark.svg)

This repository contains Kubernetes configurations and deployment scripts for containerized applications. It provides a structured approach to deploying applications on Kubernetes clusters.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)


## Features

- Ready-to-use Kubernetes manifests for deployments, services, and configurations
- Organized directory structure for different Kubernetes resources
- Sample configurations for common application setups
- Scalable deployment patterns
- Best practices for Kubernetes resource management

## Prerequisites

Before using this project, ensure you have:

- [kubectl](https://kubernetes.io/docs/tasks/tools/) installed
- Access to a Kubernetes cluster (Minikube, Kind, or cloud provider)
- [Docker](https://docs.docker.com/get-docker/) installed (for building images)
- Basic understanding of Kubernetes concepts

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vinayak-dhaka/Kubernetes_pj.git
   cd Kubernetes_pj
   pip install -r requirements.txt
   cd backend
2. Run backend :
```bash
   uvicorn main:app --reload
```
3. Run frontend:
   index.html
