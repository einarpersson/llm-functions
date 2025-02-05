import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.nvim_rpc import get_nvim
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

    nvim = get_nvim()

    return nvim.exec_lua(f"return require('aichat_utils').replace_text({json.dumps(search, ensure_ascii=False)}, {json.dumps(replace, ensure_ascii=False)})")

