import json
import xml.etree.ElementTree as Element_tree
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplayStrategy(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplayStrategy(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class PrinterStrategy(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class ConsolePrinterStrategy(PrinterStrategy):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinterStrategy(PrinterStrategy):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = Element_tree.Element("book")
        title = Element_tree.SubElement(root, "title")
        title.text = book.title
        content = Element_tree.SubElement(root, "content")
        content.text = book.content
        return Element_tree.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:

    display_strategies = {
        "console": ConsoleDisplayStrategy(),
        "reverse": ReverseDisplayStrategy(),
    }

    print_strategies = {
        "console": ConsolePrinterStrategy(),
        "reverse": ReversePrinterStrategy(),
    }

    serializers = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            strategy = display_strategies.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown display type: {method_type}")
            strategy.display(book)

        elif cmd == "print":
            strategy = print_strategies.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown print type: {method_type}")
            strategy.print(book)

        elif cmd == "serialize":
            serializer = serializers.get(method_type)
            if not serializer:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
