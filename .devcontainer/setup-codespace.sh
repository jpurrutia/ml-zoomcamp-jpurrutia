#!/bin/bash
set -e

echo "🚀 Setting up ML Zoomcamp Codespace environment..."

# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.cargo/env

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate
uv sync --extra dev

echo "✅ Codespace setup complete!"
echo "📊 Environment: Codespaces (limited resources)"
echo "💡 Tip: Use small datasets and batch sizes in this environment"