import pyfiglet
import sys
from typing import Tuple


def format(text:str, font:str|None="lean", *, file=sys.stdout.write) -> Tuple[int, int]:
    """
    ``` python
    format() -> (numpass, numfail)
    ```

    Args:
        text (str): text to format
        font (str, None, optional): font for text format. Defaults to "lean".
        file (optional): tool to write to. Defaults to sys.stdout.write.

    Returns:
        Tuple[int, int]: (numpass, numfail)
    """
    try:
        file(pyfiglet.figlet_format(text, width=90)
             if(font is None)
             else pyfiglet.figlet_format(text, font))
        return (1, 0)
    except:
        return (0, 1)


__all__ = ["format"]
