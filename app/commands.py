from abc import ABC, abstractmethod

from app.book import Book
from app.serializers import XmlSerializer, JsonSerializer


class BaseCommand(ABC):
    def __init__(self, method_type: str, book: Book) -> None:
        self.method_type = method_type
        self.book = book

    @abstractmethod
    def execute(self) -> None:
        pass


class DisplayCommand(BaseCommand):
    def execute(self) -> None:
        self.book.display(self.method_type)


class PrintCommand(BaseCommand):
    def execute(self) -> None:
        self.book.print_book(self.method_type)


class SerializeCommand(BaseCommand):
    def execute(self) -> str:
        if self.method_type == "xml":
            serializer = XmlSerializer(self.book.title, self.book.content)
            return serializer.serialize()
        elif self.method_type == "json":
            serializer = JsonSerializer(self.book.title, self.book.content)
            return serializer.serialize()
        else:
            raise ValueError(f"Unknown serialize type: {self.method_type}")
