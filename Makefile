.PHONY: help install install-dev install-all clean test format lint notebook

help:
	@echo "Available commands:"
	@echo "  make install      - Install base dependencies"
	@echo "  make install-dev  - Install with dev tools"
	@echo "  make install-all  - Install everything (including GPU libs)"
	@echo "  make test        - Run tests"
	@echo "  make format      - Format code with black"
	@echo "  make lint        - Lint code with ruff"
	@echo "  make notebook    - Start Jupyter notebook"
	@echo "  make clean       - Clean cache files"

install:
	uv sync

install-dev:
	uv sync --extra dev

install-all:
	uv sync --all-extras

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache
	rm -rf .ruff_cache

test:
	pytest tests/

format:
	black .
	ruff check --fix .

lint:
	ruff check .
	black --check .

notebook:
	jupyter notebook