from typing import Any, Callable

def longest(arr: Any):
    if not arr:
        return None
    
    return max(arr, key=len)

class _help:
    def __init__(self, cmds: dict[str, dict[Callable, str]]) -> None:
        self.cmds: dict[str, dict[Callable, str]] = cmds

    def __call__(self) -> None:
        print("Commands:")
        for cmd in self.cmds:
            spcs = " " * (len(longest(self.cmds.keys())) - len(cmd))
            print(f"  {cmd}{spcs} - {self.cmds[cmd]['desc']}")
