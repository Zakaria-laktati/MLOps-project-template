from sklearn.externals import joblib
import pandas as pd

def load_model(model_path):
    """Load the trained model from the specified path."""
    model = joblib.load(model_path)
    return model

def make_predictions(model, input_data):
    """Make predictions using the trained model."""
    predictions = model.predict(input_data)
    return predictions

if __name__ == "__main__":
    # Example usage
    model_path = "path/to/your/model.pkl"  # Update with your model path
    input_data_path = "path/to/your/input_data.csv"  # Update with your input data path

    # Load the model
    model = load_model(model_path)

    # Load input data
    input_data = pd.read_csv(input_data_path)

    # Make predictions
    predictions = make_predictions(model, input_data)

    # Output predictions
    print(predictions)