from pathlib import Path

import joblib
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split


DATA_DIR = Path("data")
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"


def prepare_datasets(test_size: float = 0.2, random_state: int = 42) -> None:

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    dataset = fetch_california_housing(as_frame=True)
    df = dataset.frame

    raw_path = RAW_DIR / "california_housing_raw.parquet"
    df.to_parquet(raw_path, index=False)

    X = df.drop(columns=["MedHouseVal"])
    y = df["MedHouseVal"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    joblib.dump(X_train, PROCESSED_DIR / "X_train.joblib")
    joblib.dump(X_test, PROCESSED_DIR / "X_test.joblib")
    joblib.dump(y_train, PROCESSED_DIR / "y_train.joblib")
    joblib.dump(y_test, PROCESSED_DIR / "y_test.joblib")


if __name__ == "__main__":
    prepare_datasets()
import pandas as pd
import os

def load_raw_data(data_path):
    """Load raw data from the specified path."""
    raw_data_files = [f for f in os.listdir(data_path) if f.endswith('.csv')]
    dataframes = []
    for file in raw_data_files:
        df = pd.read_csv(os.path.join(data_path, file))
        dataframes.append(df)
    return pd.concat(dataframes, ignore_index=True)

def transform_data(df):
    """Transform the raw data into a suitable format for analysis."""
    # Example transformation: drop duplicates and fill missing values
    df = df.drop_duplicates()
    df = df.fillna(method='ffill')
    return df

def save_processed_data(df, output_path):
    """Save the processed data to the specified output path."""
    df.to_csv(output_path, index=False)

def main():
    raw_data_path = '../data/raw'
    interim_data_path = '../data/interim/processed_data.csv'
    
    # Load raw data
    raw_data = load_raw_data(raw_data_path)
    
    # Transform data
    processed_data = transform_data(raw_data)
    
    # Save processed data
    save_processed_data(processed_data, interim_data_path)

if __name__ == "__main__":
    main()