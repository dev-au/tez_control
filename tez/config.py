import configparser
import os

from .schemas import Tez, Server, Project


def load_config() -> Tez:
    try:
        config_file_name = ".tez"
        location = os.path.join(os.getcwd(), config_file_name)

        if not os.path.exists(location):
            raise FileNotFoundError(f"Configuration file '{config_file_name}' not found.")

        config = configparser.ConfigParser()
        config.read(location)

        server_config = {
            "host": config.get("server", "SERVER_HOST", fallback=None),
            "user": config.get("server", "SERVER_USER", fallback=None),
            "password": config.get("server", "SERVER_PASSWORD", fallback=None),
            "port": config.getint("server", "SERVER_PORT", fallback=None),
        }

        server_commands = {}
        if config.has_section("server-commands"):
            server_commands = {command: terminal_command for command, terminal_command in
                               config.items("server-commands")}

        local_commands = {}
        if config.has_section("local-commands"):
            local_commands = {command: terminal_command for command, terminal_command in config.items("local-commands")}
        project_config = {
            "path": config.get("project", "PROJECT_PATH", fallback=None),
        }

        return Tez(
            server=Server(**server_config),
            server_commands=server_commands,
            local_commands=local_commands,
            project=Project(**project_config),
        )
    except Exception as e:
        print(f"Error loading config: {e}")
        return Tez(
            server=Server(host=None, port=None, user=None, password=None),
            project=Project(path=None),
            server_commands={},
            local_commands={}
        )
