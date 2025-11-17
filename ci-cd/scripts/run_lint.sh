#!/bin/bash

# Run linting on the source code using flake8
flake8 src/ --max-line-length=120

# Optionally, you can add other linters or formatters here, such as black or isort
# black src/
# isort src/