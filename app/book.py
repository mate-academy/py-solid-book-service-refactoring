import json
from xml.etree import ElementTree
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class BookDisplayer(ABC):
    @staticmethod
    @abstractmethod
    def display(book: Book) -> None:
        pass


class ConsoleBookDisplayer(BookDisplayer):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content)


class ReverseBookDisplayer(BookDisplayer):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content[::-1])


class BookPrinter(ABC):
    @staticmethod
    @abstractmethod
    def print_book(book: Book, displayer: BookDisplayer) -> None:
        pass


class ConsoleBookPrinter(BookPrinter):
    @staticmethod
    def print_book(
        book: Book,
        displayer: BookDisplayer = ConsoleBookDisplayer
    ) -> None:
        print(f"Printing the book: {book.title}...")
        displayer.display(book)


class ReverseBookPrinter(BookPrinter):
    @staticmethod
    def print_book(
        book: Book,
        displayer: BookDisplayer = ReverseBookDisplayer
    ) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        displayer.display(book)


class BookSerializer(ABC):
    @staticmethod
    @abstractmethod
    def serialize(book: Book) -> str:
        pass


class JSONBookSerializer(BookSerializer):
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLBookSerializer(BookSerializer):
    @staticmethod
    def serialize(book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


class DisplayBookHandler:
    strategies = {
        "console": ConsoleBookDisplayer,
        "reverse": ReverseBookDisplayer,
    }

    @staticmethod
    def execute(book: Book, display_type: str) -> None:
        displayer = DisplayBookHandler.strategies.get(display_type)

        if displayer is None:
            raise ValueError(f"Unknown display type: {display_type}")

        displayer.display(book)


class PrintBookHandler:
    strategies = {
        "console": ConsoleBookPrinter,
        "reverse": ReverseBookPrinter,
    }

    @staticmethod
    def execute(book: Book, print_type: str) -> None:
        printer = PrintBookHandler.strategies.get(print_type)

        if printer is None:
            raise ValueError(f"Unknown print type: {print_type}")

        printer.print_book(book)


class SerializeBookHandler:
    strategies = {
        "json": JSONBookSerializer,
        "xml": XMLBookSerializer,
    }

    @staticmethod
    def execute(book: Book, serialize_type: str) -> str:
        serializer = SerializeBookHandler.strategies.get(serialize_type)

        if serializer is None:
            raise ValueError(f"Unknown serialize type: {serialize_type}")

        return serializer.serialize(book)
