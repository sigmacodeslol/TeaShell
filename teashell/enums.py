__all__ = ["tsht", "TSHt_inputprocessor"]

from enum import Enum


class TSHt(Enum):
    """Docstring for TSHt."""

    FUNCTYPE = "tsht:functype"
    NONFUNCTYPE = "tsht:nonfunctype"
    NULL = "tsht:NULL"
    REGULAR = "tsht:regular"
    SETDEFAULTTYPE = "tsht:setdefaulttype"
    TASKABORT = "tsht:taskabort"


class TSHt_inputprocessor(Enum):
    """Docstring for TSHt_inputprocessor"""

    UPDATE_SET_ABORT = "tsht.in#prc:updatesetabort"
    SUCCESS_UPDATE_SET = "tsht.in#prc: successupdateset"
