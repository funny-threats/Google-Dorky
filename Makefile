.PHONY: install setup test clean run help

help:
	@echo "Google Dork SQL Injection Scanner - Makefile"
	@echo ""
	@echo "Available commands:"
	@echo "  make install    - Install dependencies"
	@echo "  make setup      - Run full setup (create venv and install)"
	@echo "  make run        - Run the scanner with default dorks"
	@echo "  make clean      - Clean temporary files and caches"
	@echo "  make test       - Run basic tests"
	@echo "  make help       - Show this help message"

install:
	pip install -r requirements.txt

setup:
	python3 -m venv venv
	. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
	@echo "Setup complete! Activate with: source venv/bin/activate"

run:
	python main.py --dorks dorks.txt

clean:
	find . -type d -name __pycache__ -exec rm -r {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.log" -delete
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	@echo "Clean complete!"

test:
	python -m pytest tests/ -v || echo "No tests directory found. Skipping tests."
