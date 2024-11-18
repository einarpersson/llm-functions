import pynvim
import os
import json

def run(new_text: str) -> str:
    """Replace all text in the current buffer.

    Args:
        new_text: The new text to replace the buffer with. Can contain multiple lines.
    Returns:
        A status message.

    Example:
        {
          "new_text": "This is a new version of the text\nAnother sentence.",
        }
    """

    rpc_address = os.environ.get("RPC_ADDRESS")

    if rpc_address is None:
        return "Neovim RPC_ADDRESS not set."

    try:
        nvim = pynvim.attach("socket", path=rpc_address)
    except FileNotFoundError:
        return "Neovim RPC socket not found. Please start the server first."

    return nvim.exec_lua(f"return require('aichat_utils').replace_buffer({json.dumps(new_text, ensure_ascii=False)})")

