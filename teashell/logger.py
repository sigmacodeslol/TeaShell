from datetime import datetime
import os
from pathlib import Path
from typing import Callable

from _err import Terminate
from grhh import grhh
from stdfio import _Path
from scripts.cleanup_logs import cleanup


class LWrite:
    def __init__(self, lfrom: str, lmsg: str, ltype: str) -> None:
        self.lfrom: str = lfrom
        self.lmsg: str = lmsg
        self.ltype: str = ltype

        self._exitc: int = None

    def exit(self, exitcode: int = 0) -> None:
        self._exitc = exitcode


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
        max_logs = self._config["logging"]["max_logs"]
        if num_files > max_logs:
            cleanup(self._log_dir)
            cleaned: bool = True
        else:
            cleaned: bool = False

        # write the log
        lw: LWrite = args[0]
        PATH = _Path(Path(self._logfp))
        if PATH.path.exists():
            PATH._append(f"\n({lw.lfrom})[{lw.ltype}]: {lw.lmsg}")
        else:
            if cleaned:
                PATH._write(
                    f"(logger)[cleanup]: cleaned logs folder (count: {max_logs + 1})"
                )
            PATH._write(f"({lw.lfrom})[{lw.ltype}]: {lw.lmsg}")

        if lw._exitc is not None:
            PATH._append(f"\n(logger)[exit]: {lw._exitc}")


__all__ = ["_LOG", "LWrite"]
