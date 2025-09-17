#!/usr/bin/env python3
"""Download and prepare datasets for ML Zoomcamp"""

import os
import sys
from pathlib import Path
import requests
from tqdm import tqdm
import zipfile
import argparse

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))
from config.settings import detect_environment, Environment

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

DATASETS = {
    "sample": {
        "url": "https://example.com/sample_data.zip",
        "size": "10MB",
        "description": "Small sample dataset for development"
    },
    "full": {
        "url": "https://example.com/full_data.zip",
        "size": "2GB",
        "description": "Full dataset for training"
    }
}

def download_file(url: str, destination: Path, description: str = ""):
    """Download file with progress bar"""
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(destination, 'wb') as f:
        with tqdm(total=total_size, unit='B', unit_scale=True, desc=description) as pbar:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                pbar.update(len(chunk))

def main():
    parser = argparse.ArgumentParser(description="Download ML Zoomcamp datasets")
    parser.add_argument("--dataset", choices=["sample", "full", "auto"],
                       default="auto", help="Which dataset to download")
    args = parser.parse_args()

    # Auto-detect based on environment
    if args.dataset == "auto":
        env = detect_environment()
        dataset_key = "sample" if env == Environment.CODESPACES else "full"
        print(f"🔍 Detected {env.value} environment, downloading {dataset_key} dataset")
    else:
        dataset_key = args.dataset

    dataset = DATASETS[dataset_key]
    print(f"📊 Downloading {dataset['description']} ({dataset['size']})")

    # Download logic here
    # download_file(dataset["url"], DATA_DIR / f"{dataset_key}.zip")

    print("✅ Download complete!")

if __name__ == "__main__":
    main()