import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.nvim_rpc import get_nvim

def run(chunk: str) -> str:
    """This function executes a chunk of lua code in the current neovim session over RPC. The returning value will be converted to a string. 

    Will be executed in the following way:
    ```
    return vim.inspect((function()
    {chunk}
    end)())
    ```

    Args:
        chunk: The lua code to execute, as a function body.
    Returns:
        A string representation of the return value of the lua code.

    Example:
        {
          "chunk": "return vim.diagnostic.get()"
        }
    """

    nvim = get_nvim()

    chunk_to_execute = f"""
    return vim.inspect((function()
    {chunk}
    end)())
    """

    return nvim.exec_lua(chunk_to_execute)

