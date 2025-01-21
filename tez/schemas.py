from dataclasses import dataclass
from typing import List, Dict, Optional, Callable


@dataclass
class Server:
    host: Optional[str]
    port: Optional[int]
    user: Optional[str]
    password: Optional[str]


@dataclass
class Project:
    path: Optional[str]



@dataclass
class Tez:
    server: Server
    project: Project
    server_commands: Dict[str, str]
    local_commands: Dict[str, 10]
