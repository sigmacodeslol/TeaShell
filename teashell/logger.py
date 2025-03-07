from datetime import datetime

from grhh import grhh


class _LOG:
    def __init__(self) -> None:
        now: str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        mod_strf: dict = {"now": now, "rhh": grhh(2), "ftype": "log"}
        self._logf: str = "%(now)s+%(rhh)s.%(ftype)s" % mod_strf
        print(self._logf)


__all__ = ["_LOG"]
