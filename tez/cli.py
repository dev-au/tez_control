import argparse
import re
from invoke import UnexpectedExit
from termcolor import colored

from .config import load_config
from .handlers import action_custom_server_command, action_custom_local_command
from .server_session import enter_live_server
from .colored_print import colored_print
from .genete_example import generate_local_config

def replace_placeholders(command, args):
    """Replace $1, $2, ... in the command with actual arguments."""
    for i, arg in enumerate(args, start=1):
        command = re.sub(rf"\${i}\b", arg, command)  # Replace placeholders
    return command

def main():
    parser = argparse.ArgumentParser(description="Project Commands")
    settings = load_config()

    parser.add_argument("command", nargs='+', help="Command to execute")
    args = parser.parse_args()

    cmd_key = args.command[0]  # First argument is the command key
    cmd_args = args.command[1:]  # Remaining arguments

    if cmd_key == 'sv':
        enter_live_server(settings)
        return
    if cmd_key == 'ex':
        generate_local_config()
        return

    server_handler = settings.server_commands.get(cmd_key)
    local_handler = settings.local_commands.get(cmd_key)

    if server_handler:
        server_handler = replace_placeholders(server_handler, cmd_args)
        if '$' in server_handler:
            colored_print(f"Invalid command arguments: {cmd_key}", 'red')
            return
        try:
            action_custom_server_command(f"cd {settings.project.path} && {server_handler}", settings=settings)
        except UnexpectedExit:
            pass

    elif local_handler:
        local_handler = replace_placeholders(local_handler, cmd_args)
        if '$' in local_handler:
            colored_print(f"Invalid command arguments: {cmd_key}", 'red')
            return
        try:
            action_custom_local_command(local_handler, settings=settings)
        except Exception as e:
            colored_print(str(e), color='red')

    else:
        message = f'Command "{cmd_key}" not found'
        colored_message = colored(message, 'red', attrs=['bold'])
        print(colored_message)

if __name__ == '__main__':
    main()
