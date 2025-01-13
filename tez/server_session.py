import os, pyfiglet

from fabric import Connection
from invoke import UnexpectedExit
from termcolor import colored


from .handlers import action_custom_command
from .colored_print import colored_print


def enter_live_server(settings):
    """
    Connects to the server, provides an interactive shell experience, and allows directory navigation,
    command execution, and other shell commands like clear and exit.
    """
    server_host = settings.server.host
    server_user = settings.server.user
    server_password = settings.server.password
    try:
        # Establish connection
        with Connection(
                host=server_host,
                user=server_user,
                connect_kwargs={"password": server_password}
        ) as conn:
            colored_print(f'Connecting to {server_host} as {server_user}...', 'cyan')

            # Get initial directory
            current_path = conn.run("pwd", hide=True).stdout.strip()
            os.system('clear')
            r = pyfiglet.figlet_format(f'Success')
            colored_print(r, 'green')

            while True:
                try:
                    command_input = input(colored(f"{server_user}@{server_host}:{current_path}> ", 'cyan'))
                    if command_input.lower() in ("q", "exit"):
                        colored_print('Exited Tez server', 'red')
                        break
                    elif command_input.lower() == "clear":
                        os.system('clear')
                        continue
                    elif command_input.startswith("cd "):
                        new_dir = command_input.split(' ', 1)[1]
                        try:
                            test_dir = conn.run(f"cd {os.path.join(current_path, new_dir)} && pwd",
                                                hide=True).stdout.strip()
                            current_path = test_dir
                        except UnexpectedExit:
                            colored_print(f"Directory not found: {new_dir}", "red")
                        continue
                    terminal_command = settings.commands.get(command_input)
                    if terminal_command:
                        action_custom_command(f"cd {settings.project.path} && {terminal_command}", settings=settings,
                                              server=conn)
                    else:
                        try:
                            result = conn.run(f"cd {current_path} && {command_input}", hide=True)
                            print(result.stdout.strip())
                        except Exception as e:
                            colored_print(f"{e}", 'red')

                except KeyboardInterrupt:
                    colored_print("\nCommand canceled (Ctrl+C)", "yellow")
                except EOFError:
                    colored_print("\nExited Tez server (Ctrl+D)", "red")
                    continue

    except Exception as e:
        colored_print(f"Error connecting to the server: {e}", 'red')
