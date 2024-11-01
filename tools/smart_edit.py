import pynvim
import os
import subprocess
from pathlib import Path

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

    sock_files = list(Path('/tmp/nvim.einar').rglob('*.sock'))

    rpc_address = None
    nvim = None
    for sock_file in sock_files:
        try:
            nvim = pynvim.attach("socket", path=str(sock_file))
            buffer = nvim.current.buffer
            if filename in buffer.name:
                rpc_address = str(sock_file)
                break
        except FileNotFoundError:
            continue

    if rpc_address is None:
        return "Not implemented yet."

    # Now, let's read the file contents and send it to the assistant
    if nvim is None:
        return "Neovim session not found."

    file_contents = "\n".join(nvim.current.buffer[:])

    if len(file_contents) > 100000:
        return "File too large. Limit is 100,000 characters."

    os.environ["RPC_ADDRESS"] = rpc_address
    os.environ["FILE_TO_EDIT"] = filename
    os.environ["FILE_CONTENTS"] = file_contents
    os.environ["INSTRUCTIONS"] = instructions

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

