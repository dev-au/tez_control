import argparse
import shlex

from invoke import UnexpectedExit
from termcolor import colored

from .colored_print import colored_print
from .config import load_config
from .genete_example import generate_local_config
from .handlers import action_custom_server_command, action_custom_local_command
from .server_session import enter_live_server


def serialize_command(command, args):
    queue = 0
    new_command = ''
    for e in command:
        if e == '$':
            try:
                new_command += f'"{args[queue]}"'
                queue += 1
            except IndexError:
                colored_print('Not enough arguments', 'red')
        else:
            new_command += e
    return new_command


def main():
    parser = argparse.ArgumentParser(description="Project Commands")
    settings = load_config()

    parser.add_argument("command", nargs='+', help="Command to execute")
    args = parser.parse_args()

    cmd_key = args.command[0]
    cmd_args = args.command[1:]

    if cmd_key == 'sv':
        enter_live_server(settings)
        return
    if cmd_key == 'ex':
        generate_local_config()
        return

    server_handler = settings.server_commands.get(cmd_key)
    local_handler = settings.local_commands.get(cmd_key)

    if server_handler:
        server_handler = serialize_command(server_handler, cmd_args)
        try:
            action_custom_server_command(f"cd {settings.project.path} && {server_handler}", settings=settings)
        except UnexpectedExit:
            pass

    elif local_handler:
        local_handler = serialize_command(local_handler, cmd_args)
        print(local_handler)
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
