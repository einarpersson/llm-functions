import os
import json
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.nvim_rpc import get_nvim

def run(line_nr: int, text: str) -> str:
    """Insert text into the current buffer at the specified line.

    Args:
        line_nr: Line number to insert text.
        text: Text to insert.

    Returns:
        Status message.
    """

    nvim = get_nvim()

    return nvim.exec_lua(f"return require('aichat_utils').insert_text({line_nr}, {json.dumps(text, ensure_ascii=False)})")

