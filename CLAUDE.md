# ML Zoomcamp Project Context

## Project Overview
Machine Learning Zoomcamp 2025 course work and projects.

## Environment Setup
- Uses UV for package management
- Python 3.12 required
- Supports both local and GitHub Codespaces development

## Key Commands
- `make install` - Install dependencies
- `make install-dev` - Install with dev tools
- `make install-all` - Install all extras (including GPU)
- `make notebook` - Start Jupyter
- `make test` - Run tests
- `make format` - Format code with black
- `make lint` - Lint code with ruff
- `python scripts/download_data.py` - Get datasets

## Resource Considerations
- Codespaces: Limited to 8GB RAM, use sample datasets
- Local: Full datasets and GPU training supported
- Environment auto-detection via `config/settings.py`

## Project Structure
- `/module_*` - Course modules
- `/data` - Datasets (gitignored)
- `/config` - Configuration and settings
- `/scripts` - Utility scripts
- `/.devcontainer` - GitHub Codespaces configuration

## Development Workflow
1. Run `./setup.sh` for initial setup (or `make install`)
2. Activate environment: `source .venv/bin/activate`
3. Start Jupyter: `make notebook`
4. Before commits: `make format` and `make lint`