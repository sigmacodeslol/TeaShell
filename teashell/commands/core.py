from typing import Any, Callable, Tuple

def longest(arr: Any):
    if not arr:
        return None
    
    return max(arr, key=len)

class _clsscr:
    """clear the screen.
    """
    def __init__(self) -> None:
        pass
    
    def __call__(self) -> None:
        import os; os.system('cls' if os.name == 'nt' else 'clear')
class _help:
    """display commands.
    """
    def __init__(self, cmds: dict[str, dict[Callable, str]]) -> None:
        self.cmds: dict[str, dict[Callable, str]] = cmds

    def __call__(self) -> None:
        print("Commands:")
        for cmd in self.cmds:
            spcs = " " * (len(longest(self.cmds.keys())) - len(cmd))
            print(f"  {cmd}{spcs} - {self.cmds[cmd]['desc']}")
