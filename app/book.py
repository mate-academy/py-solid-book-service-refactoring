from typing import Any
from app.displayer import Displayer
from app.printer import Printer
from app.serializer import Serializer


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class BookSerializer:
    def __init__(self, book: Book, serializers: dict[str, Serializer]) -> None:
        self.book = book
        self.serializers = serializers

    def serialize(self, serialize_type: str) -> str:
        serializer = self.serializers.get(serialize_type)
        if not serializer:
            self.raise_value_error("serialize", serialize_type)
        return serializer.serialize(self.book.title, self.book.content)

    def raise_value_error(self, type_: str, value: Any) -> None:
        raise ValueError(f"Unknown {type_} type: {value}")


class BookPrinter:
    def __init__(self, book: Book, printers: dict[str, Printer]) -> None:
        self.book = book
        self.printers = printers

    def print_book(self, print_type: str) -> None:
        printer = self.printers.get(print_type)
        if not printer:
            self.raise_value_error("print", print_type)
        printer.print(self.book.title, self.book.content)

    def raise_value_error(self, type_: str, value: Any) -> None:
        raise ValueError(f"Unknown {type_} type: {value}")


class BookDisplayer:
    def __init__(self, book: Book, displayers: dict[str, Displayer]) -> None:
        self.book = book
        self.displayers = displayers

    def display(self, display_type: str) -> None:
        displayer = self.displayers.get(display_type)
        if not displayer:
            self.raise_value_error("display", display_type)
        displayer.display(self.book.content)

    def raise_value_error(self, type_: str, value: Any) -> None:
        raise ValueError(f"Unknown {type_} type: {value}")
