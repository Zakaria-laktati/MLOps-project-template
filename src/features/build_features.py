from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

def build_features(data: pd.DataFrame) -> pd.DataFrame:
    """
    Generate features from the processed data.

    Parameters:
    data (pd.DataFrame): The input data for feature engineering.

    Returns:
    pd.DataFrame: The dataframe with engineered features.
    """
    # Example feature engineering
    data['feature_mean'] = data.mean(axis=1)
    data['feature_std'] = data.std(axis=1)
    
    # Scaling features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(data)
    
    # Creating a new DataFrame with scaled features
    feature_df = pd.DataFrame(scaled_features, columns=[f'scaled_feature_{i}' for i in range(scaled_features.shape[1])])
    
    return feature_df

if __name__ == "__main__":
    # Example usage
    # Load your processed data here
    processed_data = pd.read_csv('data/processed/your_processed_data.csv')
    features = build_features(processed_data)
    features.to_csv('data/processed/engineered_features.csv', index=False)