import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.nvim_rpc import get_nvim

def run() -> str:
    """Get diagnostics

    Returns:
        Diagnostics as a table
    """

    nvim = get_nvim()

    return nvim.exec_lua(f"return require('aichat_utils').get_diagnostics()")

