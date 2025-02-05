import os
from typing import Optional
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.nvim_rpc import get_nvim

def run(bufnr: Optional[int]) -> str:
    """Read current buffer.

    Returns:
        Buffer content
    """

    nvim = get_nvim()

    return nvim.exec_lua(f"return require('aichat_utils').read_buffer({bufnr})")

