#!/usr/bin/env python3
"""
Build script to generate OpenAPI client from specification.

This script is run during package installation to generate the FM API client.
"""

import os
import subprocess
import sys
from pathlib import Path


def generate_fm_client():
    """Generate the File Management API client from OpenAPI spec."""
    # Get the project root directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    openapi_spec = project_root / "memvid_mcp_server" / "fm_openapi.yml"
    output_path = project_root / "memvid_mcp_server" / "fm_client"
    
    print(f"Generating FM API client from {openapi_spec}...")
    print(f"Output directory: {output_path}")
    
    # Check if spec exists
    if not openapi_spec.exists():
        print(f"Warning: OpenAPI spec not found at {openapi_spec}")
        print("Skipping FM client generation.")
        return 0
    
    # Remove existing generated client
    if output_path.exists():
        import shutil
        shutil.rmtree(output_path)
        print(f"Removed existing client at {output_path}")
    
    # Generate the client
    try:
        cmd = [
            "openapi-python-client",
            "generate",
            "--path", str(openapi_spec),
            "--output-path", str(output_path),
        ]
        
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True,
        )
        
        print("✅ FM API client generated successfully!")
        if result.stdout:
            print(result.stdout)
        
        return 0
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to generate FM API client: {e}")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
        return 1
    except FileNotFoundError:
        print("❌ openapi-python-client not found!")
        print("Please install it: pip install openapi-python-client")
        return 1


if __name__ == "__main__":
    sys.exit(generate_fm_client())
