import os
from fastmcp import FastMCP

mcp = FastMCP("File Search Server")

@mcp.tool()
def search_file(file_name: str) -> list[str]:
    """
    Search the entire local drive for files matching the given file name.

    Args:
        file_name: The exact or partial name of the file to search for.

    Returns:
        A list of full paths to matching files.
    """
    matches = []
    start_dirs = []

    # Detect platform root folders
    if os.name == "nt":  # Windows
        # Get all drive letters
        import string
        from ctypes import windll

        bitmask = windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                start_dirs.append(f"{letter}:\\")
            bitmask >>= 1
    else:
        # For macOS / Linux, start from root
        start_dirs.append("/")

    for start_dir in start_dirs:
        for root, dirs, files in os.walk(start_dir, topdown=True, followlinks=False):
            # Skip system folders to avoid permission errors
            dirs[:] = [d for d in dirs if not d.startswith("$") and not d.startswith(".")]

            for f in files:
                if file_name.lower() in f.lower():
                    full_path = os.path.join(root, f)
                    matches.append(full_path)

    return matches