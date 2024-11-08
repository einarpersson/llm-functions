import pynvim
import os
# import json
# from typing import Optional

# def run(bufnr: Optional[number]) -> str:
def run() -> str:
    """Read current buffer.

    Returns:
        Buffer content
    """

    rpc_address = os.environ.get("RPC_ADDRESS")

    if rpc_address is None:
        return "Neovim RPC_ADDRESS not set."

    try:
        nvim = pynvim.attach("socket", path=rpc_address)
    except FileNotFoundError:
        return "Neovim RPC socket not found. Please start the server first."

    return nvim.exec_lua(f"return require('aichat_utils').read_buffer()")

