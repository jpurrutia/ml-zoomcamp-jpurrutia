# ML Zoomcamp Project Context

## ⚠️ IMPORTANT: Session Context Updates
**Update this file at the start of each development session with:**
- Current module/week being worked on
- Any ongoing issues or blockers
- Recent changes made
- Next planned tasks

See `log.md` for detailed session history.

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

## Current Session Context
**Last Updated:** 2025-09-17
- **Status:** Initial repository setup complete
- **Environment:** Dual support for local and Codespaces configured
- **Recent Changes:** Fixed UV installation path for new installer version
- **Next Tasks:** Test Codespaces deployment, begin Module 1 exercises