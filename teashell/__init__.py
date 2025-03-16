from typing import Callable

import art
from color import Colors
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
        self._cmds[cmd]: dict = {
            "f": func,
            "desc": func.__doc__,
        }

    def remove(self, cmd: str) -> None:
        self._cmds.pop(cmd, None)

    def get(self, cmd: str) -> Callable:
        return self._cmds.get(cmd, None)


class TeaShell:
    def __init__(self) -> None:
        self.__log = logger._LOG(config)

        self.__cmds = _CMDdb(self.__log)
        # cmd registers
        self.__cmds.register(["clear", "cls"], core._clsscr())
        self.__cmds.register("help", core._help(self.__cmds._cmds))
        self.__cmds.register("exit", None)

    def __call__(self) -> None:
        log = self.__log
        log(LWrite("msys/init", "instantiated logs module", "INFO"))  # msys: main sys
        log(LWrite("msys/init", "initialized sys global vars", "INFO"))

        check_errors = art.format("Tea-SHell")
        print(f"{Colors.DARK_GRAY}TeaShell{Colors.END}")
        if(check_errors[1] > 0):
            log(LWrite("msys/init", "failed to print teashell logo", "ERROR"))
        else:
            log(LWrite("msys/init", "successfully printed teashell logo", "INFO"))

        prompt = ""
        format_dict = {}
        if("%(shell)s" in config["prompt"]):
            format_dict["shell"] = "tsh"

        terminate = False
        while not terminate:
            usr_in: str = get_input(prompt=(config["prompt"] % {"shell": ""})).strip().replace(",", "")
            if usr_in == "":
                continue
            parsed = parse(usr_in, nonfunctypes=nonfunctypes)
            cmd: str = parsed.cmd
            args: list[str] = parsed.args
            opts: list[str] = parsed.opts
            cmdt: PXt = parsed.cmdType
            ic(cmd, args, opts, cmdt)

        log(LWrite("msys/exit", "terminated shell [code=0]", "INFO"))


tsh = (
    TeaShell()()
)  # when finished project delete second pair of brackets and write the main.py in parent folder.


__all__ = ["tsh", "TeaShell"]
