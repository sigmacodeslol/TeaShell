import yaml


def load_config() -> __import__("typing").Any:
    with open("../config.yaml", "r") as f:
        return yaml.safe_load(f)


config: __import__("typing").Any = load_config()

__all__ = ["config"]
