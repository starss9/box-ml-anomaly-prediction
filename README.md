# box-ml-anomaly-prediction
This project provides a simple API for detecting anomalies based on volume and weight inputs using a machine learning model (Isolation Forest). It's built using **FastAPI** and designed to be deployable on platforms like **Google Cloud Platform (GCP)** with Kubernetes.
##  Features

- Predict whether box dimensions (volume and weight) are normal or anomalous
- REST API built with FastAPI
- Lightweight and easy to deploy
- Model serialized with `.pkl` using scikit-learn
- Ready for Dockerization and deployment on GCP

- ##  ML Model

- Algorithm: Isolation Forest
- Input features: `volume`, `weight`
- Output: `0` (normal) or `-1` (anomaly)
- Trained and saved as `anomaly_model.pkl`
