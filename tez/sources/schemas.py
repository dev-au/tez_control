from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Server:
    host: str
    port: int
    user: str
    password: str


@dataclass
class Project:
    path: str



@dataclass
class Tez:
    server: Server
    project: Project
    commands: Dict[str, str]
