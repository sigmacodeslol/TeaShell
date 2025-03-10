from config import config
import logger
from logger import LWrite


class TeaShell:
    def __init__(self) -> None:
        self.__log = logger._LOG(config)

    def __call__(self) -> None:
        log = self.__log
        log(LWrite("msys", "initialized sys global vars", "init"))  # msys: main sys
        log(LWrite("msys", "successfully printed teashell logo", "init"))

        log(LWrite("msys", "terminated shell", "exit"))


tsh = (
    TeaShell()()
)  # when finished project delete second pair of brackets and write the main.py in parent folder.


__all__ = ["tsh", "TeaShell"]
