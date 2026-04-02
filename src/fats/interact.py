"""
Minimalist interactive REPL utility.
"""

import atexit
import code
import readline
import rlcompleter
import sys
from pathlib import Path
from typing import Any, Dict, Optional


def interact(local: Optional[Dict[str, Any]] = None, banner: Optional[str] = None, history: str = "~/.fats_history") -> None:
    """Launch an interactive REPL with history and auto-completion. Defaults to caller's globals."""
    if local is None:
        local = sys._getframe(1).f_globals

    # Configure auto-completion
    readline.set_completer(rlcompleter.Completer(local).complete)
    if "libedit" in readline.__doc__:  # macOS (libedit)
        readline.parse_and_bind("bind ^I rl_complete")
    else:  # Linux/Windows (GNU readline)
        readline.parse_and_bind("tab: complete")

    hist_path = Path(history).expanduser()
    if hist_path.exists():
        try:
            readline.read_history_file(str(hist_path))
        except (OSError, IOError):
            # Ignore history loading errors
            pass

    def _save_history() -> None:
        try:
            readline.set_history_length(history_limit)
            readline.write_history_file(str(hist_path))
        except (OSError, IOError):
            pass

    atexit.register(_save_history)

    # Prepare banner
    if banner is None:
        banner = f"\033[34m--- FATS REPL ({sys.version.split()[0]}) ---\033[0m"

    code.interact(banner=banner, local=local, exitmsg="")


if __name__ == "__main__":
    interact()
