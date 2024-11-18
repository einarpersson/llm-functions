import pynvim
import os
import json

def run(search: str, replace: str) -> str:
    """Replace text in the current buffer.

    Args:
        search: The string to search for. Has to be unique and exact.
        replace: The string to replace with.
    Returns:
        A status message.

    Example:
        {
          "search": "How many apples?\nTwo please!",
          "replace": "How many bananas?\nThree please!!"
        }
    """

    rpc_address = os.environ.get("RPC_ADDRESS")

    if rpc_address is None:
        return "Neovim RPC_ADDRESS not set."

    try:
        nvim = pynvim.attach("socket", path=rpc_address)
    except FileNotFoundError:
        return "Neovim RPC socket not found. Please start the server first."

    return nvim.exec_lua(f"return require('aichat_utils').replace_text({json.dumps(search, ensure_ascii=False)}, {json.dumps(replace, ensure_ascii=False)})")

