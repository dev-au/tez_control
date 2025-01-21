import argparse

from invoke import UnexpectedExit
from termcolor import colored

from .config import load_config
from .handlers import action_custom_server_command, action_custom_local_command
from .server_session import enter_live_server
from .colored_print import colored_print
from .genete_example import generate_local_config


def main():
    parser = argparse.ArgumentParser(description="Project Commands")
    settings = load_config()
    choices = list(settings.server_commands.keys()) + list(settings.local_commands.keys())
    choices.append('sv')
    choices.append('ex')
    parser.add_argument("command", choices=choices, help="Command to execute")
    args = parser.parse_args()
    if args.command == 'sv':
        enter_live_server(settings)
        return
    if args.command == 'ex':
        generate_local_config()
        return 
    server_handler = settings.server_commands.get(args.command, None)
    local_handler = settings.local_commands.get(args.command, None)
    if server_handler:
        try:
            action_custom_server_command(f"cd {settings.project.path} && {handler}", settings=settings)
        except UnexpectedExit:
            pass
    
    elif local_handler:
        try:
            action_custom_local_command(local_handler, settings=settings)
        except Exception as e:
            colored_print(str(e), color='red')


    else:
        message = 'Command "{}" not found'.format(args.command)
        colored_message = colored(message, 'red', attrs=['bold'])
        print(colored_message)


if __name__ == '__main__':
    main()
