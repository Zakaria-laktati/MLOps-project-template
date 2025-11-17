from pathlib import Path
import logging

import joblib
import pandas as pd
from scipy.stats import ks_2samp

from evidently.metric_preset import (
    DataDriftPreset,
    DataQualityPreset,
    RegressionPreset,
)
from evidently.report import Report


PROCESSED_DIR = Path("data") / "processed"
MODELS_DIR = Path("models")
MODEL_PATH = MODELS_DIR / "regression_model.joblib"
REPORTS_DIR = Path("monitoring") / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def _load_data():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model artifact not found at {MODEL_PATH}. Run training before monitoring."
        )

    model = joblib.load(MODEL_PATH)

    X_train = joblib.load(PROCESSED_DIR / "X_train.joblib")
    y_train = joblib.load(PROCESSED_DIR / "y_train.joblib")
    X_test = joblib.load(MODELS_DIR / "X_test_for_monitoring.joblib")
    y_test = joblib.load(MODELS_DIR / "y_test_for_monitoring.joblib")

    ref = X_train.copy()
    ref["target"] = y_train.values if hasattr(y_train, "values") else y_train
    ref["prediction"] = model.predict(X_train)

    cur = X_test.copy()
    cur["target"] = y_test.values if hasattr(y_test, "values") else y_test
    cur["prediction"] = model.predict(X_test)

    return ref, cur


def generate_evidently_report():
    ref, cur = _load_data()

    report = Report(
        metrics=[DataQualityPreset(), DataDriftPreset(), RegressionPreset()]
    )

    report.run(reference_data=ref, current_data=cur)

    html_path = REPORTS_DIR / "regression_data_report.html"
    json_path = REPORTS_DIR / "regression_data_report.json"

    print(f"Saving Evidently HTML report to {html_path}")
    report.save_html(str(html_path))
    print(f"Saving Evidently JSON report to {json_path}")
    report.save_json(str(json_path))


if __name__ == "__main__":
    generate_evidently_report()

class DataDriftMonitor:
    def __init__(self, reference_data: pd.DataFrame, current_data: pd.DataFrame, threshold: float = 0.05):
        self.reference_data = reference_data
        self.current_data = current_data
        self.threshold = threshold
        self.logger = self.setup_logger()

    def setup_logger(self):
        logger = logging.getLogger("DataDriftMonitor")
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def check_drift(self):
        drift_results = {}
        for column in self.reference_data.columns:
            if column in self.current_data.columns:
                stat, p_value = ks_2samp(self.reference_data[column], self.current_data[column])
                drift_results[column] = {
                    'statistic': stat,
                    'p_value': p_value,
                    'drift': p_value < self.threshold
                }
                self.logger.info(f"Column: {column}, Statistic: {stat}, P-value: {p_value}, Drift Detected: {drift_results[column]['drift']}")
            else:
                self.logger.warning(f"Column {column} not found in current data.")
        return drift_results

# Example usage:
# reference_data = pd.read_csv('path_to_reference_data.csv')
# current_data = pd.read_csv('path_to_current_data.csv')
# monitor = DataDriftMonitor(reference_data, current_data)
# drift_report = monitor.check_drift()