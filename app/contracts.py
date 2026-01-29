from typing import Protocol


class BookProtocol(Protocol):
    title: str
    content: str
