import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.nvim_rpc import get_nvim

def run(start: int, finish: int) -> str:
    """Delete lines in the current buffer from start to finish.

    Args:
        start: Start line number.
        finish: Finish line number.

    Returns:
        Status message.
    """

    nvim = get_nvim()

    return nvim.exec_lua(f"return require('aichat_utils').delete_range({start}, {finish})")

