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
        _w = 90
        file(pyfiglet.figlet_format(text, width=_w)
             if(font is None)
             else pyfiglet.figlet_format(text, font, width=_w))
        return (1, 0)
    except:
        return (0, 1)


__all__ = ["format"]
