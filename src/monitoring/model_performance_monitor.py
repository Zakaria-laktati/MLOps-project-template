from datetime import datetime
import logging

class ModelPerformanceMonitor:
    def __init__(self, model, threshold=0.8):
        self.model = model
        self.threshold = threshold
        self.logger = self.setup_logger()

    def setup_logger(self):
        logger = logging.getLogger("ModelPerformanceMonitor")
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler("model_performance.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def log_performance(self, metric_value):
        if metric_value < self.threshold:
            self.logger.warning(f"Model performance dropped below threshold: {metric_value}")
        else:
            self.logger.info(f"Model performance is acceptable: {metric_value}")

    def monitor(self, metric_function):
        metric_value = metric_function(self.model)
        self.log_performance(metric_value)

# Example usage:
# monitor = ModelPerformanceMonitor(model)
# monitor.monitor(evaluate_model_function)  # evaluate_model_function should return a performance metric value.