from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def __repr__(self) -> str:
        return f"Book(title='{self.title}', content='{self.content[:50]}...')"


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class PrintStrategy(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        pass


class SerializationStrategy(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class Command(ABC):
    @abstractmethod
    def execute(self) -> str | None:
        pass


class CommandFactory(ABC):
    @abstractmethod
    def create_command(self, book: Book, method_type: str) -> Command:
        pass
