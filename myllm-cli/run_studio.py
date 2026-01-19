"""
MyLLM Studio - Standalone Entry Point
Run this to start MyLLM Studio as a desktop application
"""

import sys
import os
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

def main():
    """Main entry point for MyLLM Studio"""
    try:
        import uvicorn
        from myllm.studio_server import app
        import webbrowser
        import threading
        import time

        # Print startup info
        print("=" * 50)
        print("🚀 MyLLM Studio Starting...")
        print("=" * 50)
        print()
        print("Interface will open in your browser...")
        print()
        print("URL: http://localhost:8090")
        print()
        print("Press Ctrl+C to stop the server")
        print("=" * 50)
        print()

        # Open browser after short delay
        def open_browser():
            time.sleep(2)
            try:
                webbrowser.open("http://localhost:8090")
            except:
                pass

        threading.Thread(target=open_browser, daemon=True).start()

        # Start server
        uvicorn.run(
            app,
            host="0.0.0.0",
            port=8090,
            log_level="info"
        )

    except KeyboardInterrupt:
        print("\n\nShutting down MyLLM Studio...")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error starting MyLLM Studio: {e}")
        print("\nTroubleshooting:")
        print("  1. Make sure port 8090 is not in use")
        print("  2. Check that all dependencies are installed")
        print("  3. Run: pip install -r requirements.txt")
        print()
        input("Press Enter to exit...")
        sys.exit(1)


if __name__ == "__main__":
    main()
