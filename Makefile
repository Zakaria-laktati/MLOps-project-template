# Makefile

.PHONY: all data build train serve test lint

all: data build train serve

data:
	@echo "Preparing data..."
	dvc pull

build:
	@echo "Building Docker images..."
	docker-compose build

train:
	@echo "Training the model..."
	docker-compose run training

serve:
	@echo "Starting the API server..."
	docker-compose up -d serving

test:
	@echo "Running tests..."
	./ci-cd/scripts/run_tests.sh

lint:
	@echo "Running linter..."
	./ci-cd/scripts/run_lint.sh

clean:
	@echo "Cleaning up..."
	docker-compose down
	dvc gc --workspace --force
