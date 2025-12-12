import json
import xml.etree.ElementTree as ElTr

from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class IDisplay(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class IPrinter(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ISerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class ConsoleDisplay(IDisplay):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(IDisplay):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class ConsolePrinter(IPrinter):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(IPrinter):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class JsonSerializer(ISerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(ISerializer):
    def serialize(self, book: Book) -> str:
        root = ElTr.Element("book")
        title = ElTr.SubElement(root, "title")
        title.text = book.title
        content = ElTr.SubElement(root, "content")
        content.text = book.content
        return ElTr.tostring(root, encoding="unicode")


DISPLAY_STRATEGIES = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}

PRINTER_STRATEGIES = {
    "console": ConsolePrinter(),
    "reverse": ReversePrinter(),
}

SERIALIZER_STRATEGIES = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    result = None

    for cmd, method_type in commands:
        if cmd == "display":
            if strategy := DISPLAY_STRATEGIES.get(method_type):
                strategy.display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")

        elif cmd == "print":
            if strategy := PRINTER_STRATEGIES.get(method_type):
                strategy.print_book(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")

        elif cmd == "serialize":
            if strategy := SERIALIZER_STRATEGIES.get(method_type):
                result = strategy.serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
