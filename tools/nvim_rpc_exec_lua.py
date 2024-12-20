import pynvim
import os

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

    rpc_address = os.environ.get("RPC_ADDRESS")

    if rpc_address is None:
        return "Neovim RPC_ADDRESS not set."

    try:
        nvim = pynvim.attach("socket", path=rpc_address)
    except FileNotFoundError:
        return "Neovim RPC socket not found. Please start the server first."

    # chunk_to_execute = f"return vim.print({chunk})"
    chunk_to_execute = f"""
    return vim.inspect((function()
    {chunk}
    end)())
    """

    return nvim.exec_lua(chunk_to_execute)

