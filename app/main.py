import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class ConsoleDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content[::-1])


class PrintStrategy(ABC):
    @abstractmethod
    def print(self, title: str, content: str) -> None:
        pass


class ConsolePrint(PrintStrategy):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrint(PrintStrategy):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JsonSerializer(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerializer(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        root = ElementTree.Element("book")
        title_elem = ElementTree.SubElement(root, "title")
        title_elem.text = title
        content_elem = ElementTree.SubElement(root, "content")
        content_elem.text = content
        return ElementTree.tostring(root, encoding="unicode")


class BookService:
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self, display_strategy: DisplayStrategy) -> None:
        display_strategy.display(self.book.content)

    def print_book(self, print_strategy: PrintStrategy) -> None:
        print_strategy.print(self.book.title, self.book.content)

    def serialize(self, serialize_strategy: SerializeStrategy) -> str:
        return serialize_strategy.serialize(self.book.title, self.book.content)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    service = BookService(book)
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                service.display(ConsoleDisplay())
            elif method_type == "reverse":
                service.display(ReverseDisplay())
        elif cmd == "print":
            if method_type == "console":
                service.print_book(ConsolePrint())
            elif method_type == "reverse":
                service.print_book(ReversePrint())
        elif cmd == "serialize":
            if method_type == "json":
                return service.serialize(JsonSerializer())
            elif method_type == "xml":
                return service.serialize(XmlSerializer())
