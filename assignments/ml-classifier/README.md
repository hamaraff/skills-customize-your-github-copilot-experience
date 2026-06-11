# 📘 Assignment: End-to-End ML Classifier (scikit-learn)

## 🎯 Objective

Build a small end-to-end machine learning classifier using scikit-learn: preprocess a dataset, train and evaluate multiple models, export the best model, and serve predictions via a minimal API.

## 📝 Tasks

### 🛠️ Prepare Data and Features

#### Description
Load the provided dataset, handle missing values, and engineer any simple features needed.

#### Requirements
- Use `pandas` to load and inspect the dataset (`data.csv`).
- Handle missing values and encode categorical variables if present.
- Split into features (`X`) and label (`y`).

### 🛠️ Train and Evaluate Models

#### Description
Train at least two classifiers and compare them using cross-validation.

#### Requirements
- Train at least two model types (e.g., `LogisticRegression`, `RandomForestClassifier`).
- Use cross-validation (e.g., `cross_val_score`) and report metrics: accuracy, F1, and ROC AUC where applicable.
- Select the best model based on validation performance and save it to `model.joblib`.

### 🛠️ Serve Predictions

#### Description
Create a small FastAPI endpoint that loads the trained model and returns predictions for incoming feature vectors.

#### Requirements
- Implement a prediction endpoint `POST /predict` that accepts JSON input and returns model predictions.
- Validate input with Pydantic models.
- Load `model.joblib` at startup (or train on startup if model file missing).

## 🚀 How to run (student)

Install dependencies:

```bash
pip install -r requirements.txt
```

Train and run the API (from the assignment folder):

```bash
python starter_code.py    # trains model (if needed) and writes model.joblib
uvicorn starter_code:app --reload
```

Test the prediction endpoint at `http://127.0.0.1:8000/docs`.

## 📂 Files

- `starter_code.py` — starter script: loads data, trains model, saves model, exposes FastAPI prediction endpoint.
- `data.csv` — small sample dataset for the assignment.
- `requirements.txt` — Python dependencies.

## ✅ Submission

- Submit your completed `starter_code.py` and any improvements to `data.csv` preprocessing.
- Ensure the API runs and correctly predicts using the saved `model.joblib`.

## ✨ Extensions (optional)

- Add a `/train` endpoint for re-training with new hyperparameters.
- Add feature importance visualization and include it in the README.
- Export the model to ONNX and compare inference latency.

## 🎓 Learning Outcomes

- Preprocess real data with `pandas`.
- Train and evaluate classifiers with scikit-learn.
- Serialize models with `joblib`.
- Serve model predictions using FastAPI.
