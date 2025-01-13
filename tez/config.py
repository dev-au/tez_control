import configparser
import os, sys

from .schemas import Tez, Server, Project
from .colored_print import colored_print



def load_config() -> Tez:
    try:
        config_file_name = ".tez"
        possible_locations = [
            os.path.join(os.getcwd(), config_file_name),
            # os.path.expanduser(f"~/{config_file_name}"),
            # os.path.join(os.path.dirname(os.path.abspath(__file__)), config_file_name)
        ]
    
        config_file = None
        for location in possible_locations:
            if os.path.exists(location):
                config_file = location
                break
    
        if not config_file:
            raise FileNotFoundError(
                f"Configuration file '{config_file_name}' not found in current directory, home directory, or script location.")
    
        config = configparser.ConfigParser()
        config.read(config_file)
    
    
        server_config = {
            "host": config.get("server", "SERVER_HOST", fallback=None),
            "user": config.get("server", "SERVER_USER", fallback=None),
            "password": config.get("server", "SERVER_PASSWORD", fallback=None),
            "port": config.getint("server", "SERVER_PORT", fallback=None),
        }
    
        commands = {}
        for command, terminal_command in config["commands"].items():
            commands[command] = terminal_command
    
        project_config = {
            "path": config.get("project", "PROJECT_PATH", fallback=None),
        }
    
        return Tez(
            server=Server(**server_config),
            commands=commands,
            project=Project(**project_config),
        )
    except:
        return Tez(server=Server(host=None, port=None, user=None, password=None), project=Project(path=None), commands={})

