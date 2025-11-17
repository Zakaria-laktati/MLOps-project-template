from pathlib import Path

import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


PROCESSED_DIR = Path("data") / "processed"
MODELS_DIR = Path("models")
MODELS_DIR.mkdir(exist_ok=True)


def _load_datasets():
    X_train = joblib.load(PROCESSED_DIR / "X_train.joblib")
    X_test = joblib.load(PROCESSED_DIR / "X_test.joblib")
    y_train = joblib.load(PROCESSED_DIR / "y_train.joblib")
    y_test = joblib.load(PROCESSED_DIR / "y_test.joblib")
    return X_train, X_test, y_train, y_test


def train_regression_model(
    n_estimators: int = 100, max_depth: int | None = None, random_state: int = 42
):
    X_train, X_test, y_train, y_test = _load_datasets()

    pipeline = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            (
                "model",
                RandomForestRegressor(
                    n_estimators=n_estimators,
                    max_depth=max_depth,
                    random_state=random_state,
                    n_jobs=-1,
                ),
            ),
        ]
    )

    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    model_path = MODELS_DIR / "regression_model.joblib"
    joblib.dump(pipeline, model_path)

    joblib.dump(X_test, MODELS_DIR / "X_test_for_monitoring.joblib")
    joblib.dump(y_test, MODELS_DIR / "y_test_for_monitoring.joblib")

    return {"mse": mse, "r2": r2, "model_path": str(model_path)}


if __name__ == "__main__":
    metrics = train_regression_model()
    print(metrics)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pandas as pd
import joblib
import os

def train_model(data_path, model_path, test_size=0.2, random_state=42):
    # Load the dataset
    data = pd.read_csv(data_path)
    
    # Split the dataset into features and target variable
    X = data.drop('target', axis=1)
    y = data['target']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    # Initialize the model
    model = RandomForestClassifier(random_state=random_state)
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    
    # Save the trained model
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)

if __name__ == "__main__":
    train_model(data_path='data/processed/dataset.csv', model_path='models/model.joblib')