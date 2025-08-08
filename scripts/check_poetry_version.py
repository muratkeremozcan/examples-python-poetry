#!/usr/bin/env python
import subprocess
import sys
import os


def main():
    # Read expected version from .poetry-version
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    version_file = os.path.join(project_root, ".poetry-version")

    with open(version_file, "r") as f:
        expected_version = f.read().strip()

    # Get installed Poetry version
    try:
        result = subprocess.run(
            ["poetry", "--version"], capture_output=True, text=True, check=True
        )
        # Parse version from output like "Poetry (version 2.1.2)"
        installed_version = result.stdout.strip().split(" ")[-1].strip(")")

        if installed_version != expected_version:
            print(f"⚠️  Warning: Poetry version mismatch!")
            print(f"   Installed: {installed_version}")
            print(f"   Expected:  {expected_version}")
            print(f"   Consider updating your Poetry version.")
            return 1
        else:
            print(f"✓ Poetry version {installed_version} matches expected version")
            return 0
    except Exception as e:
        print(f"Error checking Poetry version: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
