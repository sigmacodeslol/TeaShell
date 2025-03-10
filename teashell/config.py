import yaml
from pathlib import Path


def load_config() -> __import__("typing").Any:
    current_dir = Path(__file__).parent
    config_yaml = str(current_dir.parent / "config.yaml")
    with open(config_yaml, "r") as f:
        return yaml.safe_load(f)


config: __import__("typing").Any = load_config()
config["exit_codes"] = {
    "success": 0,
    "error": 1,
    "invalid_argument": 2,
    "file_not_found": 2,
    "syntax_error": 2,
    "io_error": 5,
    "permission_denied": 13,
    "command_not_found": 127,
    "interrupted": 130,
}

__all__ = ["config"]
