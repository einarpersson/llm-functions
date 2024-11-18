import pynvim
import os
import json

def run(line_nr: int, text: str) -> str:
    """Insert text into the current buffer at the specified line.

    Args:
        line_nr: Line number to insert text.
        text: Text to insert.

    Returns:
        Status message.
    """

    rpc_address = os.environ.get("RPC_ADDRESS")

    if rpc_address is None:
        return "Neovim RPC_ADDRESS not set."

    try:
        nvim = pynvim.attach("socket", path=rpc_address)
    except FileNotFoundError:
        return "Neovim RPC socket not found. Please start the server first."

    return nvim.exec_lua(f"return require('aichat_utils').insert_text({line_nr}, {json.dumps(text, ensure_ascii=False)})")

