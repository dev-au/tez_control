from dataclasses import dataclass
from typing import List, Dict, Optional


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
    commands: Dict[str, str]
