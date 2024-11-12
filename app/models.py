from abc import ABC


class ContentData(ABC):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class Book(ContentData):
    pass
