#!/bin/bash
set -e

echo "🚀 Setting up ML Zoomcamp Codespace environment..."

# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# UV now installs to ~/.local/bin, add to PATH
export PATH="$HOME/.local/bin:$PATH"

# Also check the old cargo location just in case
if [ -f "$HOME/.cargo/env" ]; then
    source $HOME/.cargo/env
fi

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate
uv sync --extra dev

echo "✅ Codespace setup complete!"
echo "📊 Environment: Codespaces (limited resources)"
echo "💡 Tip: Use small datasets and batch sizes in this environment"