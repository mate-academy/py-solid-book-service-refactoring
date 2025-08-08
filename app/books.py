from dataclasses import dataclass


@dataclass
class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content
