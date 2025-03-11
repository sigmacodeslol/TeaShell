from typing import Callable


class _help:
    def __init__(self, cmds: dict[str, Callable]) -> None:
        self.cmds: dict[str, Callable] = cmds

    def __call__(self) -> None:
        print("Commands:")
        for cmd in self.cmds:
            print(f"  {cmd}")
