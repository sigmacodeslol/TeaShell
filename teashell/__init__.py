import logger
from logger import LWrite

# print(logger._LOG()(LWrite("msys", "initialized sys global vars", "init")))


class TeaShell:
    def __init__(self) -> None:
        self.__log = logger._LOG()

    def __call__(self) -> None:
        log = self.__log
        log(LWrite("msys", "initialized sys global vars", "init"))

        

        log(LWrite("msys", "terminated shell", "exit"))


tsh = (
    TeaShell()()
)  # when finished project delete second pair of brackets and write the main.py in parent folder.


__all__ = ["tsh", "TeaShell"]
