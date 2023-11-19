from abc import ABC


class Base(ABC):
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content
