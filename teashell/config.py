import yaml
from pathlib import Path


def load_config() -> __import__("typing").Any:
    current_dir = Path(__file__).parent
    config_yaml = str(current_dir.parent / "config.yaml")
    with open(config_yaml, "r") as f:
        return yaml.safe_load(f)


config: __import__("typing").Any = load_config()

__all__ = ["config"]
