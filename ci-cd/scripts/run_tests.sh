#!/bin/bash

# Run unit tests
echo "Running unit tests..."
pytest tests/unit

# Run integration tests
echo "Running integration tests..."
pytest tests/integration

# Run end-to-end tests
echo "Running end-to-end tests..."
pytest tests/e2e

echo "All tests completed."