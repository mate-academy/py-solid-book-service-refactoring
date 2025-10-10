from abc import ABC, abstractmethod
from serializers import Serializer, Json, Xml


class Book(ABC):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    @abstractmethod
    def display(self) -> None:
        pass

    @abstractmethod
    def print_book(self) -> None:
        pass

    def serialize(self, serializer: Serializer) -> str:
        return serializer.serialize()


class ConsoleBook(Book):
    def display(self) -> None:
        print(self.content)

    def print_book(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)


class ReverseBook(Book):
    def display(self) -> None:
        print(self.content[::-1])

    def print_book(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])
