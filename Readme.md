# Kubernetes Project Deployment
Working Link : https://67eb7b3602afc75d81781716--golden-sopapillas-bed010.netlify.app/
![Kubernetes Logo](https://upload.wikimedia.org/wikipedia/commons/3/39/Kubernetes_logo_without_workmark.svg)

This repository contains Kubernetes configurations and deployment scripts for containerized applications. It provides a structured approach to deploying applications on Kubernetes clusters.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)


## Pod Failure = 1
This means the model has detected a pod failure scenario.

A "pod failure" is when a Kubernetes pod (which holds one or more containers) crashes or becomes unhealthy.

1 means "yes, failure detected"
0 would mean "no failure"

Pod failures can happen due to:

CrashLoopBackOff (container crashing in loop)
OOMKilled (ran out of memory)
ImagePull errors
Unhealthy liveness/readiness probes

🌐 Network Issue = 1
This means the model has predicted a network-related issue inside the cluster.

Could be DNS resolution issues
Node/pod not able to reach the internet or other pods
Service discovery failing
Flaky inter-pod connectivity

1 means: network issue detected
0 means: network seems fine


