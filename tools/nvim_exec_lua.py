import pynvim

def run(chunk: str) -> str:
    """This function executes lua code in the current neovim session over RPC. It only evaluates statements. Expressions have to be prepended with return.
    Args:
        chunk: The lua code to execute
    Returns:
        A list of strings representing the lines read from the buffer

    Example:
        "return vim.diagnostic.get()" -> returns a list of diagnostics
    """

    rpc_address = "/tmp/nvim_aichat.sock"

    try:
        nvim = pynvim.attach("socket", path=rpc_address)
    except FileNotFoundError:
        return "Neovim RPC socket not found. Please start the server first."

    return nvim.exec_lua(chunk)

