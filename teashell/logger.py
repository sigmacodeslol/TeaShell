from dataclasses import dataclass
from datetime import datetime
import os
from pathlib import Path
from typing import Callable

from _err import Terminate
from grhh import grhh
from scripts.cleanup_logs import cleanup


@dataclass
class LWrite:
    lfrom: str
    lmsg: str
    ltype: str


class _LOG:
    """CANNOT HAVE MORE THAN ONE INSTANCE OF THIS CLASS"""

    def __init__(self, _config) -> None:
        self._config = _config

        now: str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        mod_strf: dict = {"now": now, "rhh": grhh(8), "ftype": "log"}
        self._logf: str = "%(now)s+%(rhh)s.%(ftype)s" % mod_strf

        current_dir = Path(__file__).parent
        self._log_dir = current_dir.parent / "logs"
        self._logfp = str(self._log_dir / self._logf)

    def __call__(self, mode: LWrite):
        if isinstance(mode, LWrite):
            self._write(mode)
        else:
            raise Terminate("Invalid mode for _LOG")

    def _write(self, *args, **kwargs):
        # empty the log folder if it has more than the max logs attr in config.yaml
        folder = self._log_dir
        num_files = sum(1 for entry in os.scandir(folder) if entry.is_file())
        if num_files > self._config["logging"]["max_logs"]:
            cleanup(self._log_dir)

        # write the log
        lw: LWrite = args[0]
        if Path(self._logfp).exists():
            with open(self._logfp, "a") as logf:
                logf.write(f"\n({lw.lfrom})[{lw.ltype}]: {lw.lmsg}")
        else:
            with open(self._logfp, "w") as logf:
                logf.write(f"({lw.lfrom})[{lw.ltype}]: {lw.lmsg}")


__all__ = ["_LOG", "LWrite"]
