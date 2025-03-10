"""std file io"""

from pathlib import Path


class _Path:
    def __init__(self, path: Path) -> None:
        self.__p: Path = path

    def _write(self, content: str) -> None:
        self.__p.write_text(content)

    def _append(self, content: str) -> None:
        self.__p.open("a").write(content)


__all__ = ["_Path"]
