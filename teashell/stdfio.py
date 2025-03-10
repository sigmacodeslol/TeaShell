"""std file io"""

from pathlib import Path


class _Path:
    def __init__(self, path: Path) -> None:
        self.__p: Path = path


__all__ = ["_Path"]
