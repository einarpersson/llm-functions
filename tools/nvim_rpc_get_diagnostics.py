import pynvim
import os

def run() -> str:
    """Get diagnostics

    Returns:
        Diagnostics as a table
    """

    rpc_address = os.environ.get("RPC_ADDRESS")

    if rpc_address is None:
        return "Neovim RPC_ADDRESS not set."

    try:
        nvim = pynvim.attach("socket", path=rpc_address)
    except FileNotFoundError:
        return "Neovim RPC socket not found. Please start the server first."

    return nvim.exec_lua(f"return require('aichat_utils').get_diagnostics()")

