import pynvim

def run(chunk: str) -> str:
    """This function executes lua code in the current neovim session over RPC. It only evaluates statements. Expressions have to be prepended with return. The lua code should only return strings.
    Args:
        chunk: The lua code to execute
    Returns:
        A list of strings representing the lines read from the buffer

    Example:
        Fetch diagnostics: "return vim.diagnostic.get()"
        Append a line to the buffer: "vim.api.nvim_buf_set_lines(0, -1, -1, false, {'Hello, World!'})"
    """

    rpc_address = "/tmp/nvim_aichat.sock"

    try:
        nvim = pynvim.attach("socket", path=rpc_address)
    except FileNotFoundError:
        return "Neovim RPC socket not found. Please start the server first."

    return nvim.exec_lua(chunk)

