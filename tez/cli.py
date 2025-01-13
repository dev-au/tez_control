import argparse

from invoke import UnexpectedExit
from termcolor import colored

from .config import load_config
from .handlers import action_custom_command
from .server_session import enter_live_server
from .colored_print import colored_print
from .genete_example import generate_local_config


def main():
    parser = argparse.ArgumentParser(description="Project Commands")
    settings = load_config()
    choices = list(settings.commands.keys())
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
    handler = settings.commands.get(args.command, None)
    if handler:
        try:
            action_custom_command(f"cd {settings.project.path} && {handler}", settings=settings)
        except UnexpectedExit:
            pass

    else:
        message = 'Command "{}" not found'.format(args.command)
        colored_message = colored(message, 'red', attrs=['bold'])
        print(colored_message)


if __name__ == '__main__':
    main()
