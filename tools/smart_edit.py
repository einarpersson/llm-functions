import pynvim
import time
import os
import subprocess
from pathlib import Path

def find_nvim_instance(filename: str) -> tuple[pynvim.Nvim | None, str | None]:
    """Find a running Neovim instance that has the specified file open.

    Args:
        filename: The file to look for in Neovim buffers

    Returns:
        A tuple of (nvim_instance, rpc_address). Both will be None if no suitable instance is found.
    """
    sock_files = list(Path('/tmp/nvim.einar').rglob('*.sock'))

    for sock_file in sock_files:
        try:
            nvim = pynvim.attach("socket", path=str(sock_file))
            buffer = nvim.current.buffer
            if filename in buffer.name:
                return nvim, str(sock_file)
        except FileNotFoundError:
            continue

    return None, None

def run(filename: str, instructions: str) -> str:
    """Edit a file with natural language instructions. 

    Args:
        filename: The file to edit (eg. text file, code)
        instructions: The editing instructions to execute. May contain snippets, instructions, or a combination of both. The instructions must be unambiguous and clear. Do not make the instructions solve programming problems, PROVIDE SNIPPETS and explain where you want it.
    Returns:
        A status message.

    Example 1:
        {
          "filename": "/path/to/file",
          "instructions": "replace 'foo' with 'bar'"
        }

    Example 2:
        {
          "filename": "/script.js",
          "instructions": "\n
          ```\n
          function foo() { return 'bar'; }.\n
          ```\n
          Insert this snippet after the first function declaration."
        }

    """

    nvim, rpc_address = find_nvim_instance(filename)

    if rpc_address is None:
        # Start a new headless Neovim instance and let it run for the duration of the request

        subprocess.run(["nvim", "--headless"], capture_output=True)
        # wait for the nvim instance to start
        time.sleep(1)
        nvim, rpc_address = find_nvim_instance(filename)

    if nvim is None or rpc_address is None:
        return "Neovim session not found."

    file_contents = "\n".join(nvim.current.buffer[:])
    if len(file_contents) > 100000:
        return "File too large. Limit is 100,000 characters."

    os.environ["RPC_ADDRESS"] = rpc_address
    os.environ["FILE_TO_EDIT"] = filename
    os.environ["FILE_CONTENTS"] = file_contents
    os.environ["INSTRUCTIONS"] = instructions

    if os.environ.get('DEBUG', '').lower() == 'true':
        print(f"RPC_ADDRESS: {os.environ['RPC_ADDRESS']}")
        print(f"FILE_TO_EDIT: {os.environ['FILE_TO_EDIT']}")
        print(f"FILE_CONTENTS length: {len(os.environ['FILE_CONTENTS'])}")
        print(f"INSTRUCTIONS: {os.environ['INSTRUCTIONS']}")

    response = subprocess.run(["aichat", "-r", "file", "Execute."],
                        capture_output=True,
                        text=True)

    if response.returncode != 0:
        return f"Error: {response.stderr}"

    return response.stdout

# TODOS:
# - Implement the case that there is no nvim session with the file open
# - Implement the case that there is a nvim session but it is not the current buffer, or the file is not in any open buffer

