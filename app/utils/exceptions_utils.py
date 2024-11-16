from dataclasses import dataclass

@dataclass
class AlreadyExistsException(Exception):
    message: str
    status_code: int = 409

