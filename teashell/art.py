import pyfiglet


def format(text: str, font: str = "lean"):
    return pyfiglet.figlet_format(text, font)
