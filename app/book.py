from abc import ABC


class IBook(ABC):
    title: str
    content: str


class Book(IBook):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content
