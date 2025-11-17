import pytest
from src.models.train_model import train_model

def test_train_model():
    # Assuming train_model returns a model object and takes in a dataset
    dataset = "path/to/dataset"  # Replace with actual dataset path or mock
    model = train_model(dataset)
    
    assert model is not None
    assert hasattr(model, 'predict')  # Check if the model has a predict method
    assert hasattr(model, 'score')  # Check if the model has a score method

def test_train_model_invalid_data():
    invalid_dataset = "path/to/invalid_dataset"  # Replace with actual invalid dataset path or mock
    with pytest.raises(ValueError):
        train_model(invalid_dataset)