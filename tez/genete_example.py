import os
from pathlib import Path
from .colored_print import colored_print
from .config import load_config


def generate_local_config():
    """
    Generates the .tez configuration file in the home directory
    and writes the provided configuration for the server and project.
    """

    # Path to the home directory
    home_dir = Path(os.getcwd())
    tez_file_path = home_dir / ".tez"

    # Check if the home directory is correct
    print(f"Home directory: {home_dir}")

    # Configuration content
    tez_content = f"""
    [server]
SERVER_HOST=
SERVER_USER=
SERVER_PASSWORD=
SERVER_PORT=

[project]
PROJECT_PATH=

[commands]
view=dir
    """

    # Write to .tez file
    try:
        with open(tez_file_path, "w") as tez_file:
            tez_file.write(tez_content.strip())
        colored_print(f"Generated example .tez configuration file at: {tez_file_path}", "green")
    except Exception as e:
        print(f"Failed to write .tez file: {e}")

    # Rest of the generate logic (e.g., service and nginx config generation)
    # Continue with existing logic...
