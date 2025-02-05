import os
import glob
import pynvim

def get_nvim() -> pynvim.Nvim:
    """Get a pynvim.Nvim instance for the current working directory.
    """
    user = os.getenv('USER')
    pattern = f'/tmp/nvim.{user}/*/*.sock'
    sockets = glob.glob(pattern)
    cwd = os.getcwd()

    if not sockets:
        raise FileNotFoundError("No Neovim RPC sockets found. Please start the server first.")

    # Now we want to find the instance that matches the current working directory
    matching_nvim = None
    for socket in sockets:
        nvim = pynvim.attach('socket', path=socket)
        if nvim.eval('getcwd()') == cwd:
            matching_nvim = nvim
            break

    if not matching_nvim:
        raise FileNotFoundError(f"No Neovim RPC server running in the current working directory: {cwd}.")

    return matching_nvim

