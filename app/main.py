import json
import xml.etree.ElementTree as ElTree
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class IBookDisplay(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(IBookDisplay):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseConsoleDisplay(IBookDisplay):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class IBookPrinter(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrinter(IBookPrinter):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReverseConsolePrinter(IBookPrinter):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class IBookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(IBookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(IBookSerializer):
    def serialize(self, book: Book) -> str:
        root = ElTree.Element("book")
        title = ElTree.SubElement(root, "title")
        title.text = book.title
        content = ElTree.SubElement(root, "content")
        content.text = book.content
        return ElTree.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_strategies = {
        "console": ConsoleDisplay(),
        "reverse": ReverseConsoleDisplay(),
    }

    print_strategies = {
        "console": ConsolePrinter(),
        "reverse": ReverseConsolePrinter(),
    }

    serialize_strategies = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            display_strategy = display_strategies.get(method_type)
            if display_strategy is None:
                raise ValueError(f"Unknown display type: {method_type}")
            display_strategy.display(book)
        elif cmd == "print":
            print_strategy = print_strategies.get(method_type)
            if print_strategy is None:
                raise ValueError(f"Unknown print type: {method_type}")
            print_strategy.print_book(book)
        elif cmd == "serialize":
            serialize_strategy = serialize_strategies.get(method_type)
            if serialize_strategy is None:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serialize_strategy.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
