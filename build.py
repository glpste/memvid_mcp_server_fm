"""
Custom build hooks for memvid-mcp-server.

Generates the FM API client during build.
"""

import subprocess
import sys
from pathlib import Path


def generate_client():
    """Run the client generation script."""
    script_path = Path(__file__).parent / "scripts" / "generate_fm_client.py"
    
    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            check=False,  # Don't fail build if generation fails
            capture_output=True,
            text=True,
        )
        
        # Print output regardless of success
        if result.stdout:
            print(result.stdout, file=sys.stderr)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        
        if result.returncode != 0:
            print("Warning: FM client generation failed, but continuing build.", file=sys.stderr)
            print("FM integration will not be available.", file=sys.stderr)
        
    except Exception as e:
        print(f"Warning: Could not generate FM client: {e}", file=sys.stderr)
        print("FM integration will not be available.", file=sys.stderr)
