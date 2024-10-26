from abc import ABC, abstractmethod


class Publication(ABC):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    @abstractmethod
    def type_name(self) -> str:
        pass


class Book(Publication):
    def type_name(self) -> str:
        return "book"


class Magazine(Publication):
    def type_name(self) -> str:
        return "magazine"
