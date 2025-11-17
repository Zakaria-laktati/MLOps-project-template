import pytest
from src.pipelines.training_pipeline import TrainingPipeline

def test_training_pipeline():
    # Initialize the training pipeline
    pipeline = TrainingPipeline()

    # Run the pipeline
    result = pipeline.run()

    # Check if the result is as expected
    assert result is not None, "The training pipeline should return a result."
    assert isinstance(result, dict), "The result should be a dictionary."
    assert "model" in result, "The result should contain a trained model."
    assert "metrics" in result, "The result should contain evaluation metrics."