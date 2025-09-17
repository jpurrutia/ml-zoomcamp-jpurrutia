import os
import psutil
from dataclasses import dataclass
from enum import Enum

class Environment(Enum):
    LOCAL = "local"
    CODESPACES = "codespaces"
    UNKNOWN = "unknown"

@dataclass
class ResourceConfig:
    """Adaptive configuration based on available resources"""
    batch_size: int
    max_workers: int
    memory_limit_gb: float
    use_gpu: bool
    data_sample_rate: float  # For development environments

def detect_environment() -> Environment:
    """Detect if running in Codespaces, locally, or unknown"""
    if os.environ.get("CODESPACES") == "true":
        return Environment.CODESPACES
    elif os.path.exists("/Users/jpurrutia"):  # Adjust to your local setup
        return Environment.LOCAL
    return Environment.UNKNOWN

def get_resource_config() -> ResourceConfig:
    """Get resource configuration based on environment"""
    env = detect_environment()
    memory_gb = psutil.virtual_memory().total / (1024**3)
    cpu_count = psutil.cpu_count()

    if env == Environment.CODESPACES:
        # Conservative settings for Codespaces
        return ResourceConfig(
            batch_size=32,
            max_workers=min(2, cpu_count),
            memory_limit_gb=min(4, memory_gb * 0.5),
            use_gpu=False,
            data_sample_rate=0.1  # Use 10% of data
        )
    else:
        # Full resources locally
        try:
            import torch
            has_gpu = torch.cuda.is_available()
        except ImportError:
            has_gpu = False

        return ResourceConfig(
            batch_size=256,
            max_workers=cpu_count - 1,
            memory_limit_gb=memory_gb * 0.8,
            use_gpu=has_gpu,
            data_sample_rate=1.0  # Use full data
        )

# Usage example:
# from config.settings import get_resource_config
# config = get_resource_config()
# model.fit(X, y, batch_size=config.batch_size)