import os
import json
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.nvim_rpc import get_nvim

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

    nvim = get_nvim()

    return nvim.exec_lua(f"return require('aichat_utils').replace_buffer({json.dumps(new_text, ensure_ascii=False)})")

