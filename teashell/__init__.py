from typing import Callable

import art
from commands import *
from config import config
import logger
from logger import LWrite


class Cmd:
    def __init__(self, f: Callable) -> None:
        self.f: Callable = f

    def __call__(self, *args, **kwargs) -> None:
        self.f(*args, **kwargs)


class _CMDdb:
    def __init__(self, _log: logger._LOG) -> None:
        self._cmds: dict = {}
        self._log: logger._LOG = _log

    def register(self, cmd: str, func: Callable) -> None:
        self._cmds[cmd]: Callable = func

    def remove(self, cmd: str) -> None:
        self._cmds.pop(cmd, None)

    def get(self, cmd: str) -> Callable:
        return self._cmds.get(cmd, None)


class TeaShell:
    def __init__(self) -> None:
        self.__log = logger._LOG(config)

        self.__cmds = _CMDdb(self.__log)
        # cmd registers
        self.__cmds.register("help", core._help(self.__cmds._cmds))

    def __call__(self) -> None:
        log = self.__log

        log(LWrite("msys", "initialized sys global vars", "init"))  # msys: main sys

        check_errors = art.format("TeaSHell")
        if(check_errors[1] > 0):
            log(LWrite("msys", "failed to print teashell logo", "init"))
        else:
            log(LWrite("msys", "successfully printed teashell logo", "init"))

        log(LWrite("msys", "terminated shell", "exit"))


tsh = (
    TeaShell()()
)  # when finished project delete second pair of brackets and write the main.py in parent folder.


__all__ = ["tsh", "TeaShell"]
