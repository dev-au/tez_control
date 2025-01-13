from fabric import Connection

from .config import settings
from .colored_print import colored_print


def action_custom_command(terminal_command: str, server=None) -> str:
    """
    Connects to the server, and do given commands
    """
    server_host = settings.server.host
    server_user = settings.server.user
    server_password = settings.server.password
    conn = server if server else Connection(
        host=server_host,
        user=server_user,
        connect_kwargs={"password": server_password}
    )
    with conn:
        result = conn.run(terminal_command)
        colored_print(result.stdout, 'green')
