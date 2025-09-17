#!/bin/bash
set -e

echo "🔧 ML Zoomcamp Development Setup"
echo "================================"

# Detect OS
OS="$(uname -s)"
case "${OS}" in
    Linux*)     OS_TYPE=Linux;;
    Darwin*)    OS_TYPE=Mac;;
    *)          OS_TYPE="UNKNOWN:${OS}"
esac

echo "📍 Detected OS: ${OS_TYPE}"

# Install UV if not present
if ! command -v uv &> /dev/null; then
    echo "📦 Installing UV..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # UV now installs to ~/.local/bin, add to PATH
    export PATH="$HOME/.local/bin:$PATH"
    # Also check the old cargo location just in case
    if [ -f "$HOME/.cargo/env" ]; then
        source $HOME/.cargo/env
    fi
else
    echo "✅ UV already installed: $(uv --version)"
fi

# Create and activate virtual environment
echo "🐍 Setting up Python environment..."
uv venv
source .venv/bin/activate

# Install dependencies based on environment
if [ "$CODESPACES" == "true" ]; then
    echo "☁️  Installing Codespaces dependencies..."
    uv sync --extra dev
else
    echo "💻 Installing local dependencies..."
    echo "Include GPU libraries? (y/n)"
    read -r response
    if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
        uv sync --all-extras
    else
        uv sync --extra dev
    fi
fi

echo ""
echo "✅ Setup complete!"
echo "📝 Run 'source .venv/bin/activate' to activate the environment"