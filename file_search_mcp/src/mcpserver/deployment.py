import os
from fastmcp import FastMCP

mcp = FastMCP("File Search Server")


def default_search_path():
    """Return the user's home directory as default search path (cross-OS)."""
    return os.path.expanduser("~")

@mcp.tool()
def find_file(file_name: str, search_path: str = default_search_path()) -> list[str]:
    """
    Search for a file by name starting from a given directory.
    Args:
        file_name: Name of the file to search for (case-insensitive)
        search_path: Directory to start searching from (defaults to home folder)
    Returns:
        List of matching file paths
    """
    matches = []
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file_name.lower() in file.lower():
                matches.append(os.path.join(root, file))
    return matches

@mcp.tool()
def read_file(file_path: str, start_line: int = 0, max_lines: int = 100) -> dict:
    """
    Read the contents of a file in chunks.
    Args:
        file_path: Full path to the file.
        start_line: The line number to start reading from.
        max_lines: Maximum number of lines to read.
    Returns:
        Dict containing lines read, next_start_line, and total_lines.
    """
    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}

    if not os.path.isfile(file_path):
        return {"error": f"Not a file: {file_path}"}

    lines = []
    total_lines = 0

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for idx, line in enumerate(f):
                total_lines += 1
                if idx >= start_line and len(lines) < max_lines:
                    lines.append(line.rstrip("\n"))
    except Exception as e:
        return {"error": str(e)}

    next_start = start_line + len(lines)
    return {
        "file_path": file_path,
        "lines": lines,
        "next_start_line": next_start if next_start < total_lines else None,
        "total_lines": total_lines
    }