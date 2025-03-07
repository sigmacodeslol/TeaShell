"""generate random hex hash"""

import secrets


def grhh(hexlen: int = 8) -> str:
    """generate random hex hash"""
    return secrets.token_hex(hexlen // 2)


__all__ = ["grhh"]
