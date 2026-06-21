from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET


class Book:

    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


class DisplayStrategy(ABC):

    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class PrinterStrategy(ABC):

    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class SerializerStrategy(ABC):

    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class ConsoleDisplay(DisplayStrategy):

    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayStrategy):

    def display(self, book: Book) -> None:
        print(book.content[::-1])


class ConsolePrinter(PrinterStrategy):

    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(PrinterStrategy):

    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class JsonSerializer(SerializerStrategy):

    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(SerializerStrategy):

    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


class StrategyFactory:
    _display_strategies = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }
    _print_strategies = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter(),
    }
    _serialize_strategies = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }

    @classmethod
    def get_display(cls, method_type: str) -> DisplayStrategy:
        if method_type not in cls._display_strategies:
            raise ValueError(f"Unknown display type: {method_type}")
        return cls._display_strategies[method_type]

    @classmethod
    def get_print(cls, method_type: str) -> PrinterStrategy:
        if method_type not in cls._print_strategies:
            raise ValueError(f"Unknown print type: {method_type}")
        return cls._print_strategies[method_type]

    @classmethod
    def get_serialize(cls, method_type: str) -> SerializerStrategy:
        if method_type not in cls._serialize_strategies:
            raise ValueError(f"Unknown serialize type: {method_type}")
        return cls._serialize_strategies[method_type]


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            strategy = StrategyFactory.get_display(method_type)
            strategy.display(book)
        elif cmd == "print":
            strategy = StrategyFactory.get_print(method_type)
            strategy.print_book(book)
        elif cmd == "serialize":
            strategy = StrategyFactory.get_serialize(method_type)
            return strategy.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
