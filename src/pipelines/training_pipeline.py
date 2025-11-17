from src.data.make_dataset import prepare_datasets
from src.models.train_model import train_regression_model
from src.monitoring.data_drift_monitor import generate_evidently_report


def run_training_pipeline():
    prepare_datasets()
    metrics = train_regression_model()
    print(metrics)
    generate_evidently_report()


if __name__ == "__main__":
    run_training_pipeline()
from src.data.make_dataset import load_data
from src.features.build_features import create_features
from src.models.train_model import train_model
from src.models.evaluate_model import evaluate_model
import logging

def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Step 1: Load data
    logging.info("Loading data...")
    raw_data = load_data()
    
    # Step 2: Create features
    logging.info("Creating features...")
    features = create_features(raw_data)
    
    # Step 3: Train model
    logging.info("Training model...")
    model = train_model(features)
    
    # Step 4: Evaluate model
    logging.info("Evaluating model...")
    evaluation_results = evaluate_model(model, features)
    
    logging.info("Training pipeline completed successfully.")
    logging.info(f"Evaluation Results: {evaluation_results}")

if __name__ == "__main__":
    main()