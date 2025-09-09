import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


class DisplayStrategy(ABC):
    @abstractmethod
    def render(self, book: Book) -> str:
        pass


class ConsoleDisplay(DisplayStrategy):
    def render(self, book: Book) -> str:
        return book.content


class ReverseDisplay(DisplayStrategy):
    def render(self, book: Book) -> str:
        return book.content[::-1]


class Printer(ABC):
    @abstractmethod
    def print(self, book: Book, strategy: DisplayStrategy) -> None:
        pass


class ConsolePrinter(Printer):
    def print(self, book: Book, strategy: DisplayStrategy) -> None:
        print(f"Printing the book: {book.title}...")
        print(strategy.render(book))


class ReversePrinter(Printer):
    def print(self, book: Book, strategy: DisplayStrategy) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(strategy.render(book))


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                print(ConsoleDisplay().render(book))
            elif method_type == "reverse":
                print(ReverseDisplay().render(book))
            else:
                raise ValueError(f"Unknown display type: {method_type}")

        elif cmd == "print":
            if method_type == "console":
                ConsolePrinter().print(book, ConsoleDisplay())
            elif method_type == "reverse":
                ReversePrinter().print(book, ReverseDisplay())
            else:
                raise ValueError(f"Unknown print type: {method_type}")

        elif cmd == "serialize":
            if method_type == "json":
                return JsonSerializer().serialize(book)
            elif method_type == "xml":
                return XmlSerializer().serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
