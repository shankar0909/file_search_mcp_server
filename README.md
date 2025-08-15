# Sample MCP Server

This is a sample MCP server with the following tools:

---

## 1. `find_file`

Returns the complete path of a file when provided with the **file name** and **parent directory**.

```python
"""
Search for a file by name starting from a given directory.

Args:
    file_name: Name of the file to search for (case-insensitive)
    search_path: Directory to start searching from (defaults to home folder)

Returns:
    List of matching file paths
"""
```

---

## 2. `read_file`

Returns the content of a file when provided with the **file path**.  
*Note: There are content size limitations.*

```python
"""
Read the contents of a file in chunks.

Args:
    file_path: Full path to the file.
    start_line: The line number to start reading from.
    max_lines: Maximum number of lines to read.

Returns:
    Dict containing:
        - lines read
        - next_start_line
        - total_lines
"""
```

---

## MCP Server Configuration

Add the following configuration to your MCP host/client:

```json
"File Search Server": {
  "command": "uvx",
  "args": [
    "--from",
    "git+https://github.com/shankar0909/file_search_mcp_server.git#subdirectory=file_search_mcp",
    "file-search-server"
  ]
}
```
