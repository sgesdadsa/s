"""
Test script to verify MyLLM CLI installation
"""

import sys
import subprocess
from pathlib import Path


def run_command(command):
    """Run a shell command and return success status"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)


def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    required_modules = [
        'click',
        'llama_cpp',
        'fastapi',
        'uvicorn',
        'pydantic',
        'rich',
        'requests',
        'yaml',
        'tabulate'
    ]

    failed = []
    for module in required_modules:
        try:
            __import__(module)
            print(f"  ✓ {module}")
        except ImportError:
            print(f"  ✗ {module}")
            failed.append(module)

    return len(failed) == 0, failed


def test_cli_installed():
    """Test if myllm CLI is installed"""
    print("\nTesting CLI installation...")
    success, stdout, stderr = run_command("myllm --version")

    if success:
        print("  ✓ myllm command is available")
        return True
    else:
        print("  ✗ myllm command not found")
        print(f"  Error: {stderr}")
        return False


def test_config_created():
    """Test if configuration directory is created"""
    print("\nTesting configuration...")
    config_dir = Path.home() / ".myllm"

    if config_dir.exists():
        print(f"  ✓ Config directory exists: {config_dir}")
        return True
    else:
        print(f"  ✗ Config directory not found: {config_dir}")
        return False


def test_commands():
    """Test basic commands"""
    print("\nTesting CLI commands...")

    commands = [
        ("myllm --help", "Help command"),
        ("myllm config show", "Config show"),
        ("myllm ls", "List models"),
    ]

    all_success = True
    for command, description in commands:
        success, stdout, stderr = run_command(command)
        if success:
            print(f"  ✓ {description}")
        else:
            print(f"  ✗ {description}")
            all_success = False

    return all_success


def main():
    """Run all tests"""
    print("=" * 60)
    print("MyLLM CLI Installation Test")
    print("=" * 60)
    print()

    results = []

    # Test imports
    success, failed = test_imports()
    results.append(("Module imports", success))
    if not success:
        print(f"\n  Missing modules: {', '.join(failed)}")
        print("  Install with: pip install -r requirements.txt")

    # Test CLI installation
    success = test_cli_installed()
    results.append(("CLI installation", success))

    # Test config
    success = test_config_created()
    results.append(("Configuration", success))

    # Test commands
    success = test_commands()
    results.append(("CLI commands", success))

    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)

    all_passed = True
    for test_name, success in results:
        status = "✓ PASS" if success else "✗ FAIL"
        print(f"{status} - {test_name}")
        if not success:
            all_passed = False

    print()

    if all_passed:
        print("🎉 All tests passed! MyLLM CLI is ready to use.")
        print()
        print("Next steps:")
        print("  1. Set your models directory:")
        print("     myllm config set models_directory /path/to/models")
        print()
        print("  2. List your models:")
        print("     myllm ls")
        print()
        print("  3. Load a model:")
        print("     myllm load <model-name>")
        print()
        print("  4. Start chatting:")
        print("     myllm chat")
        return 0
    else:
        print("❌ Some tests failed. Please check the errors above.")
        print()
        print("Common fixes:")
        print("  - Install dependencies: pip install -r requirements.txt")
        print("  - Install CLI: pip install -e .")
        print("  - Run myllm at least once to create config")
        return 1


if __name__ == "__main__":
    sys.exit(main())
