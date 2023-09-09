from abc import ABC


class ObjectWithContent(ABC):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class Book(ObjectWithContent):
    pass
