import os
import pandas as pd
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

DATA_FILE = "data.csv"
MODEL_FILE = "model.joblib"

app = FastAPI()

class PredictionRequest(BaseModel):
    features: List[float]

def load_data(path=DATA_FILE):
    return pd.read_csv(path)

def train_and_select_model(df):
    if 'label' not in df.columns:
        raise ValueError('Dataset must include a "label" column')
    X = df.drop(columns=['label'])
    y = df['label']

    # Simple train/test split for quick feedback
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    models = {
        'logreg': Pipeline([('scale', StandardScaler()), ('clf', LogisticRegression(max_iter=1000))]),
        'rf': Pipeline([('scale', StandardScaler()), ('clf', RandomForestClassifier(n_estimators=100))]),
    }

    best_score = -1
    best_name = None
    for name, model in models.items():
        scores = cross_val_score(model, X_train, y_train, cv=5, scoring='f1_macro')
        mean_score = scores.mean()
        print(f"Model {name} mean F1 (cv): {mean_score:.4f}")
        if mean_score > best_score:
            best_score = mean_score
            best_name = name

    best_model = models[best_name]
    best_model.fit(X_train, y_train)
    joblib.dump(best_model, MODEL_FILE)
    print(f"Trained and saved model: {best_name} (F1 {best_score:.4f})")
    return best_model

# Ensure a model exists at startup
if not os.path.exists(MODEL_FILE):
    print("Model file not found — training from data.csv")
    df = load_data()
    train_and_select_model(df)

# Load model
model = joblib.load(MODEL_FILE)

@app.post('/predict')
def predict(req: PredictionRequest):
    try:
        features = [req.features]
        pred = model.predict(features)
        return {"prediction": pred.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == '__main__':
    # Allow running the trainer directly
    df = load_data()
    train_and_select_model(df)
    print('Training complete. Start the API with: uvicorn starter_code:app --reload')
