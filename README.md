# 💳 Real-Time Fraud Detection System

An end-to-end machine learning fraud detection system built using the highly imbalanced Credit Card Fraud Detection dataset from Kaggle. The project focuses on detecting rare fraudulent transactions in real time using advanced machine learning techniques, feature engineering, explainable AI, and deployment-ready architecture.

The system integrates:
- Machine Learning models (Logistic Regression & XGBoost)
- SMOTE-based imbalance handling
- SHAP explainability
- FastAPI backend
- Streamlit frontend
- Real-time fraud prediction pipeline

---

# 📌 Problem Statement

Credit card fraud detection is a highly imbalanced classification problem where fraudulent transactions account for only **0.172%** of the dataset. Traditional accuracy-based models fail in such scenarios because they tend to predict the majority class.

This project focuses on building a robust fraud detection pipeline optimized for:
- minority class detection
- precision-recall tradeoff
- explainability
- deployment readiness

---

# 🚀 Features

- Real-time fraud prediction system
- XGBoost and Logistic Regression models
- SMOTE for imbalance handling
- Threshold optimization for fraud detection
- SHAP visualizations for model interpretability
- Streamlit interactive frontend
- FastAPI inference backend
- Feature engineering pipeline
- Precision-Recall optimized evaluation
- Production-style ML workflow

---

# 📂 Dataset

Dataset used:
- Credit Card Fraud Detection Dataset from Kaggle

Characteristics:
- Highly imbalanced dataset
- Fraud cases: **0.172%**
- PCA-transformed anonymized features (`V1–V28`)
- Transaction amount and timestamp features

---

# ⚙️ Feature Engineering

The following feature engineering steps were performed:

## ✅ Amount Scaling
- Created `Amount_scaled` using `RobustScaler`
- Helps reduce impact of extreme transaction values

## ✅ Time Feature Transformation
- Converted raw transaction time into:
  - `Hour of the Day`
- Enabled behavioral analysis of fraud patterns over time

---

# 📊 Key Insights

Exploratory Data Analysis revealed:

- Fraudulent transactions occur disproportionately during certain hours of the day
- Fraudulent transactions show stronger anomalies in specific PCA components
- Transaction amount distribution differs significantly between fraud and legitimate transactions
- Precision-Recall metrics are significantly more reliable than accuracy for this problem

---

# 🧠 Models Used

## 1. Logistic Regression
- Baseline interpretable model
- Used `class_weight='balanced'`
- Evaluated using ROC-AUC and PR-AUC

## 2. XGBoost
- Final high-performance model
- Optimized for imbalanced classification
- Used:
  - `scale_pos_weight`
  - `aucpr` evaluation metric
  - threshold tuning

---

# 📈 Evaluation Metrics

Since the dataset is highly imbalanced, the project focuses on:

- PR-AUC (Precision-Recall AUC)
- Recall
- Precision
- F1-score
- ROC-AUC

instead of relying only on accuracy.

---

# 🔍 Explainable AI with SHAP

Implemented SHAP (SHapley Additive exPlanations) to interpret model predictions.

Used SHAP for:
- Feature importance analysis
- Fraud-driving factor visualization
- Understanding individual transaction predictions
- Global model interpretability

This helps make the model more transparent and trustworthy.

---

# 🏗️ System Architecture

```text
Streamlit Frontend
        ↓
FastAPI Backend
        ↓
XGBoost Fraud Detection Model
        ↓
Real-Time Prediction Response

# 🖥️ Tech Stack

## Machine Learning
- Python
- Scikit-learn
- XGBoost
- SHAP
- Pandas
- NumPy

## Backend
- FastAPI
- Uvicorn

## Frontend
- Streamlit

## Deployment & Utilities
- Joblib
- Requests
- JSON

## Development Environment
- Jupyter Notebook
- VS Code
- macOS

---

# 🐳 Docker Support (Planned)

Future versions of the project will include Docker containerization for:
- Easier deployment
- Environment consistency
- Scalability
- Cloud-native deployment workflows

Planned Docker setup:
- Dockerfile for backend and frontend services
- Containerized FastAPI backend
- Streamlit frontend container
- Docker Compose integration

---

# ☁️ Future Deployment Plans

The project is planned to be deployed on:
- AWS
- Render
- Railway
- Streamlit Cloud

with production-grade improvements such as:
- API authentication
- Database integration
- Real-time transaction streaming
- Monitoring and logging
- CI/CD pipelines
