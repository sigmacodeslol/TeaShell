"""std file io"""

from pathlib import Path

from _err import Terminate
from config import config


class _Path:
    def __init__(self, path: Path) -> None:
        self.__p: Path = path

    @property
    def path(self) -> Path:
        return self.__p

    @path.setter
    def path(self, new) -> None:
        raise Terminate(
            "unknown unauthorised access attempt to set current path",
            code=config["exit_codes"]["permission_denied"],
        )

    def _write(self, content: str) -> None:
        self.__p.write_text(content)

    def _append(self, content: str) -> None:
        self.__p.open("a").write(content)


__all__ = ["_Path"]
