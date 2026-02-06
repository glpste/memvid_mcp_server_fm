# Memvid MCP Server 🎥

A Model Context Protocol (MCP) server that exposes Memvid video memory functionalities to AI clients. This server allows you to encode text, PDFs, and other content into video memory format for efficient semantic search and chat interactions.

**NEW**: Remote storage integration with File Management API for per-project video memory backup and synchronization.

## 🌟 Features

- **Text Encoding**: Add text chunks or full text documents to video memory
- **PDF Processing**: Extract and encode content from PDF files
- **Video Memory Building**: Generate compressed video representations of your data
- **Semantic Search**: Query your encoded data using natural language
- **Chat Interface**: Have conversations with your encoded knowledge base
- **Remote Storage**: Automatically upload video memories to File Management API (optional)
- **Background Uploads**: Non-blocking uploads that don't interrupt your workflow
- **Remote Management**: List, download, and manage remotely stored memories
- **Multi-Connection Support**: Handle multiple concurrent client connections
- **Comprehensive Logging**: Detailed logging to stderr for debugging
- **Graceful Shutdown**: Proper resource cleanup and signal handling

## 📋 Requirements

- Python 3.10 or higher
- uv package manager
- memvid package
- MCP-compatible client (e.g., Claude Desktop)

## 🚀 Installation

### 1. Set up the environment
```bash
cd /memvid_mcp_server
uv venv --python 3.12 --seed
source .venv/bin/activate
```

### 2. Install dependencies
```bash
uv add -e .
```

### 3. Generate FM API Client (Required for Remote Storage)
If you plan to use the File Management API integration, generate the client:
```bash
source .venv/bin/activate
python scripts/generate_fm_client.py
```

**Note**: This step is required only if you want to use remote storage features. The server will work without it, but FM integration tools will not be available.

### 4. H.265 Encoding with Docker

The server automatically manages Docker installation and lifecycle:

1. **Automatic Docker Setup**: If Docker is not installed, the server will install it automatically
2. **Container Management**: The memvid package handles its own Docker container building and management  
3. **Lifecycle Management**: Docker daemon is started when MCP server starts

The memvid package (installed in the venv) contains all necessary Docker configurations and will automatically:
- Build the `memvid-h265` container when needed
- Use Docker for H.265 encoding when `codec='h265'` is specified
- Handle all container lifecycle internally

No manual Docker setup or external repository paths are required.h265` using the `Dockerfile` located in the `docker/` directory.

Once the Docker image is built, `memvid` will automatically detect and use it when `video_codec='h265'` is specified in `build_video`.

### 5. Test the server (optional)
```bash
uv run python memvid_mcp_server/main.py
```
```

## ⚙️ Configuration

### Claude Desktop Setup

1. Copy the example configuration:
```bash
cp example_mcp_config.json ~/.config/claude-desktop/config.json
```

2. Or manually add to your Claude Desktop config:
```json
{
  "mcpServers": {
    "memvid-mcp-server": {
      "command": "uv",
      "args": [
        "--directory",
        "/home/ty/Repositories/memvid_mcp_server",
        "run",
        "python",
        "memvid_mcp_server/main.py"
      ],
      "env": {
        "PYTHONPATH": "/home/ty/Repositories/memvid_mcp_server",
        "PYTHONWARNINGS": "ignore"
      }
    }
  }
}
```

3. Restart Claude Desktop to load the server.

### File Management API Integration (Optional)

To enable automatic remote storage of video memories, add these environment variables to your MCP config:

```json
"env": {
  "PYTHONPATH": "/home/ty/Repositories/memvid_mcp_server",
  "PYTHONWARNINGS": "ignore",
  "FM_UPLOAD_ENABLED": "true",
  "FM_API_BASE_URL": "https://your-fm-api.example.com",
  "FM_REALM_ID": "your-realm-id",
  "FM_FOLDER_ID": "your-folder-id",
  "FM_KEYCLOAK_URL": "https://your-keycloak.example.com",
  "FM_KEYCLOAK_REALM": "your-keycloak-realm",
  "FM_KEYCLOAK_CLIENT_ID": "your-client-id",
  "FM_KEYCLOAK_CLIENT_SECRET": "your-client-secret"
}
```

**Environment Variables:**
- `FM_UPLOAD_ENABLED`: Set to "true" to enable remote uploads (default: "false")
- `FM_API_BASE_URL`: Base URL of the File Management API
- `FM_REALM_ID`: The realm ID for file storage
- `FM_FOLDER_ID`: Parent folder ID for storing video memories
- `FM_KEYCLOAK_URL`: Keycloak server URL for authentication
- `FM_KEYCLOAK_REALM`: Keycloak realm name
- `FM_KEYCLOAK_CLIENT_ID`: OAuth2 client ID
- `FM_KEYCLOAK_CLIENT_SECRET`: OAuth2 client secret

**Note**: When FM integration is enabled, video memories are automatically uploaded in the background after successful builds. You can also manually trigger uploads and manage remote memories using the provided tools.

## 🛠️ Available Tools

### Core Memory Tools

### `get_server_status`
Check the current status of the memvid server including version information and FM integration status.

### `add_chunks`
Add a list of text chunks to the encoder.
- **chunks**: List of text strings to add

### `add_text`
Add a single text document to the encoder.
- **text**: Text content to add
- **metadata**: Optional metadata dictionary

### `add_pdf`
Process and add a PDF file to the encoder.
- **pdf_path**: Path to the PDF file

### `build_video`
Build the video memory from all added content. **Automatically triggers remote upload if FM integration is enabled.**
- **video_path**: Output path for the video file
- **index_path**: Output path for the index file
- **codec**: Video codec to use ('h265' or 'h264', default: 'h265')
- **show_progress**: Whether to show progress during build (default: True)
- **auto_build_docker**: Whether to auto-build docker if needed (default: True)
- **allow_fallback**: Whether to allow fallback options (default: True)

### `search_memory`
Perform semantic search on the built video memory.
- **query**: Natural language search query
- **top_k**: Number of results to return (default: 5)

### `chat_with_memvid`
Have a conversation with your encoded knowledge base.
- **message**: Message to send to the chat system

### File Management API Tools (Optional)

These tools are only available when FM integration is configured via environment variables.

### `upload_video_memory`
Manually trigger upload of video memory files to remote storage.
- **video_path**: Path to the video memory file (.mp4)
- **index_path**: Path to the index file (.json)
- **project_name**: Optional project name for organization

### `list_remote_memories`
List video memories stored remotely in the File Management API.
- **project_name**: Optional project name to filter by

### `download_video_memory`
Download video memory files from remote storage to local machine.
- **video_doc_id**: Document ID of the video file to download
- **output_dir**: Optional directory to save files (defaults to library directory)

### `get_upload_status`
Get status of background upload tasks.
- **task_id**: Optional task ID to check specific upload. If None, returns all tasks.

## 📖 Usage Workflow

### Basic Workflow
1. **Add Content**: Use `add_text`, `add_chunks`, or `add_pdf` to add your data
2. **Build Video**: Use `build_video` to create the video memory representation
3. **Search or Chat**: Use `search_memory` for queries or `chat_with_memvid` for conversations

### With Remote Storage (FM Integration Enabled)
1. **Add Content**: Use `add_text`, `add_chunks`, or `add_pdf` to add your data
2. **Build Video**: Use `build_video` - this automatically uploads to remote storage in the background
3. **Check Upload Status**: Use `get_upload_status` to monitor background uploads
4. **List Remote Memories**: Use `list_remote_memories` to see what's stored remotely
5. **Download Memories**: Use `download_video_memory` to retrieve memories from remote storage
6. **Search or Chat**: Use `search_memory` or `chat_with_memvid` as usual

**Note**: Uploads happen in the background and won't block your workflow. Local files are always saved regardless of upload success.

## 🔧 Development

### Testing
```bash
# Install development dependencies
uv add --dev pytest pytest-asyncio black ruff mypy

# Run tests
uv run pytest

# Format code
uv run black memvid_mcp_server/
uv run ruff check memvid_mcp_server/
```

### Debugging
- Check logs in Claude Desktop: `~/Library/Logs/Claude/mcp*.log` (macOS) or equivalent
- Enable debug logging by setting `LOG_LEVEL=DEBUG` in environment
- Use `get_server_status` tool to check server state

## 🔧 Troubleshooting

### Common Issues

1. **JSON Parsing Errors**: All output is properly redirected to stderr to prevent protocol interference
2. **Import Errors**: The server gracefully handles missing memvid package with clear error messages
3. **Connection Issues**: Check Claude Desktop logs and use `get_server_status` to diagnose issues
4. **Video Build Failures**: Ensure sufficient disk space and valid paths

### Logging Configuration

The server implements comprehensive stdout redirection to prevent any library output from interfering with the MCP JSON-RPC protocol:

- All memvid operations are wrapped with stdout redirection
- Progress bars, warnings, and model loading messages are captured
- Only structured JSON responses are sent to Claude Desktop
- All diagnostic information is logged to stderr

### Error Messages

- **"Memvid not available"**: Install the memvid package: `uv add memvid`
- **"Video memory not built"**: Run `build_video` before searching or chatting
- **"LLM not available"**: Expected warning - memvid will work without external LLM providers
- **"FM integration not configured"**: Set FM environment variables to enable remote storage features

### File Management (FM) Integration Issues

1. **FM Client Not Generated**
   - Run `python scripts/generate_fm_client.py` to generate the API client
   - Ensure `openapi-python-client` is installed: `uv add openapi-python-client`
   - Check that `fm_openapi.yml` exists in `memvid_mcp_server/` directory
   - Generated client will be in `memvid_mcp_server/fm_client/` (gitignored)

2. **Uploads Not Working**
   - Check that `FM_UPLOAD_ENABLED=true` is set
   - Verify all FM environment variables are correctly configured
   - Check logs for authentication errors
   - Verify network connectivity to FM API and Keycloak
   - Use `get_upload_status` to see error details

2. **Authentication Failures**
   - Verify Keycloak URL, realm, client ID, and secret are correct
   - Check that the client has proper permissions in Keycloak
   - Ensure the realm exists in the File Management system

3. **Upload Queue Errors**
   - Uploads happen in background and won't block video building
   - Check logs for detailed error messages
   - Failed uploads can be retried manually with `upload_video_memory`

4. **Missing Remote Memories**
   - Verify you're using the correct `FM_REALM_ID` and `FM_FOLDER_ID`
   - Check that uploads completed successfully with `get_upload_status`
   - Use `list_remote_memories` to see what's actually stored

5. **Large File Upload Timeouts**
   - Default timeout is 5 minutes for uploads
   - Check network bandwidth and stability
   - Consider using a closer/faster FM API endpoint

## 📄 License

MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📚 Related Projects

- [Memvid](https://github.com/tomayac/memvid) - The underlying video memory technology
- [Model Context Protocol](https://modelcontextprotocol.io/) - The protocol specification
- [Claude Desktop](https://claude.ai/download) - MCP-compatible AI client

---

Generated with improvements for production reliability and MCP best practices.
