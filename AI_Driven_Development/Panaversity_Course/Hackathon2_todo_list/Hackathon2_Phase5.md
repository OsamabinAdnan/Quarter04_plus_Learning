# 🚀 Hackathon 2 -- Phase 5: Advanced Cloud Deployment



------------------------------------------------------------------------

## 👋 Introduction

This document is a **complete, step‑by‑step guideline** for **Hackathon 2 -- Phase 5 (Advanced Cloud
Deployment)**.

Phase 5 is the **final and most advanced phase** of the hackathon. In
this phase, we take our **AI-powered Todo Chatbot** from earlier phases
and turn it into an **enterprise‑ready, cloud‑native, event‑driven
application** using:

-   Kubernetes (Minikube → Cloud)
-   Dapr (Distributed Application Runtime)
-   Kafka (Event-driven architecture)
-   Agentic Dev Stack (Spec‑Driven Development)

⚠️ **Important Rule:**\
❌ No manual coding\
✅ Everything must be done via **Claude Code + Spec‑Kit workflow**

------------------------------------------------------------------------

## 🧠 Phase 5 Overview

Phase 5 has **three major parts**:

### **Part A -- Advanced Features**

-   Intermediate + Advanced Todo features
-   Event-driven architecture with Kafka
-   Dapr integration in app code

### **Part B -- Local Deployment**

-   Minikube testing
-   Dapr + Self‑hosted Kafka

### **Part C -- Cloud Deployment**

-   Kubernetes on Cloud (AKS / GKE / OKE)
-   Managed Kafka
-   CI/CD + Monitoring

------------------------------------------------------------------------

## 🛠️ Key Technologies Used

-   **Dapr** -- Pub/Sub, State, Jobs, Secrets, Service Invocation\
-   **Kafka** -- Event-driven architecture\
-   **Helm Charts** -- Deployment (reuse from Phase IV)\
-   **GitHub Actions** -- CI/CD\
-   **Claude Code** -- Agentic coding\
-   **Spec‑Kit Plus** -- Spec → Plan → Tasks → Implement

------------------------------------------------------------------------

## ⏱️ Expected Time

-   **10--15 days** (depends on experience)

------------------------------------------------------------------------

## 💸 Free Resources

-   **Oracle Cloud OKE** -- Always Free (Recommended)
-   **Azure** -- \$200 credits
-   **Google Cloud** -- \$300 credits (90 days)
-   **Redpanda Cloud** -- Free Kafka serverless tier

------------------------------------------------------------------------

## ✅ Prerequisites

Before starting Phase 5, ensure:

### ✔️ Completed

-   Phases 1--4
-   Working Todo Chatbot
-   Local Minikube deployment (Phase IV)

### ✔️ Accounts

-   Oracle Cloud: https://www.oracle.com/cloud/free/
-   Azure: https://azure.microsoft.com/en-us/free/
-   Google Cloud: https://cloud.google.com/free
-   Redpanda Cloud: https://redpanda.com/cloud
-   GitHub account

### ✔️ Tools Installed

-   Dapr CLI\
-   kubectl, Helm, Minikube\
-   Cloud CLI (OCI / Azure / gcloud)\
-   kafka-python\
-   GitHub

------------------------------------------------------------------------

# 📘 Step‑by‑Step Guide

------------------------------------------------------------------------

## 🧩 Part A -- Advanced Features (3--5 Days)

### 1️⃣ Update Constitution

Create **constitution.md (v5.0)** using Claude Code.

**Goal:** - Define new rules for: - Advanced features - Event-driven
architecture - Dapr + Kafka usage

------------------------------------------------------------------------

### 2️⃣ Specify Features (sp.specify)

Run:

``` bash
/sp.specify Advanced Features Integration
```

#### Intermediate Features

-   Priority (High / Medium / Low)
-   Tags (Work / Home / Personal)
-   Search & Filter
-   Sorting (date, priority, title)

#### Advanced Features

-   Recurring Tasks (daily / weekly / monthly)
-   Due Dates & Reminders

------------------------------------------------------------------------

### 3️⃣ Planning (sp.plan)

Run:

``` bash
/sp.plan Advanced Features
```

**Plan should include:** - Backend changes (models, APIs) - Frontend UI
updates - Kafka event publishing - Dapr abstraction (NO direct Kafka
code)

------------------------------------------------------------------------

### 4️⃣ Tasks & Implementation

Run:

``` bash
/sp.tasks
```

Example tasks: - Add priority field to Task model - Publish
`task-completed` event - Recurring service creates next task

✔ Backend: FastAPI + SQLModel\
✔ Frontend: Forms, filters, sorting\
✔ Events: Kafka via Dapr Pub/Sub

------------------------------------------------------------------------

### 5️⃣ Initial Dapr Setup

-   Install Dapr CLI
-   Add Dapr sidecar to backend
-   Create Dapr component YAMLs:
    -   pubsub.kafka
    -   state.postgresql

------------------------------------------------------------------------

## 🧪 Part B -- Local Deployment (2--3 Days)

### 1️⃣ Enable Dapr in Helm Charts

Add annotations:

``` yaml
dapr.io/enabled: "true"
dapr.io/app-id: "todo-backend"
dapr.io/app-port: "8000"
```

------------------------------------------------------------------------

### 2️⃣ Deploy Dapr Components

``` bash
kubectl apply -f dapr-components/
```

------------------------------------------------------------------------

### 3️⃣ Self‑Hosted Kafka (Strimzi)

``` bash
kubectl create namespace kafka
kubectl apply -f https://strimzi.io/install/latest?namespace=kafka
```

Create Kafka cluster (1 replica, ephemeral storage)

Topics: - task-events - reminders - task-updates

------------------------------------------------------------------------

### 4️⃣ Deploy on Minikube

``` bash
minikube start
dapr init -k
helm install todo-app ./charts/todo
```

✔ Test reminders\
✔ Test recurring tasks\
✔ Verify Kafka events

------------------------------------------------------------------------

## ☁️ Part C -- Cloud Deployment (4--6 Days)

### 1️⃣ Choose Cloud Provider

⭐ **Oracle OKE (Recommended -- Always Free)**\
Other options: - Azure AKS - Google GKE

------------------------------------------------------------------------

### 2️⃣ Create Kubernetes Cluster

-   Setup CLI
-   Configure kubectl
-   Verify nodes

------------------------------------------------------------------------

### 3️⃣ Managed Kafka

Use **Redpanda Cloud** - Create serverless cluster - Create topics -
Copy credentials

------------------------------------------------------------------------

### 4️⃣ Dapr on Cloud

``` bash
dapr init -k
```

Update Dapr components: - pubsub.kafka (Redpanda) - state.postgresql
(Neon DB)

------------------------------------------------------------------------

### 5️⃣ Deploy via Helm

``` bash
helm install todo-app ./charts/todo --set image.tag=latest
```

------------------------------------------------------------------------

### 6️⃣ CI/CD with GitHub Actions

Create:

``` text
.github/workflows/deploy.yaml
```

Pipeline: - Build Docker images - Push to Docker Hub - Deploy to
Kubernetes

Secrets: - COHERE_API_KEY - DB credentials

------------------------------------------------------------------------

### 7️⃣ Monitoring & Logging

-   Cloud-native monitoring
-   Optional: Prometheus + Grafana

------------------------------------------------------------------------

## 🎥 Final Testing & Demo

✔ App running on Cloud\
✔ Reminders working\
✔ Recurring tasks auto‑created\
✔ Scale test:

``` bash
kubectl scale deployment todo-backend --replicas=5
```

🎬 **Demo Video (90 seconds max):** - Features - Architecture - Cloud
deployment

------------------------------------------------------------------------

## 📦 Submission Checklist

-   ✅ Public GitHub Repository
-   ✅ Specs folder
-   ✅ AGENTS.md + CLAUDE.md
-   ✅ README.md
-   ✅ Cloud URL
-   ✅ Minikube guide
-   ✅ Demo Video (90 sec)

------------------------------------------------------------------------

## 🙌 Final Tips

-   Use **free tiers wisely**
-   Let **Dapr handle infra**
-   Follow **Spec‑Driven Development strictly**
-   Use **agents for EVERYTHING**

------------------------------------------------------------------------