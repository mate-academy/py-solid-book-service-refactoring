import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod
from typing import Optional, List, Tuple, Dict


# 1. Модель залишається простою
class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


# --- СТРАТЕГІЇ ФОРМАТУВАННЯ (Open/Closed Principle) ---

class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass


class ConsoleFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content


class ReverseFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content[::-1]


# --- СТРАТЕГІЇ СЕРІАЛІЗАЦІЇ (Open/Closed Principle) ---

class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps(
            {"title": book.title,
             "content": book.content},
            ensure_ascii=False
        )


class XmlSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        ElementTree.SubElement(root, "title").text = book.title
        ElementTree.SubElement(root, "content").text = book.content
        return ElementTree.tostring(root, encoding="unicode")


# --- ПРИНТЕР (Dependency Inversion Principle) ---

class BookPrinter:
    # Тепер він залежить від абстракції Formatter, а не від конкретного класу
    def print_book(self, book: Book, formatter: Formatter) -> None:
        formatted_content = formatter.format(book)
        print(f"--- Printing Book: {book.title} ---")
        print(formatted_content)


# --- ГОЛОВНА ФУНКЦІЯ ---

def main(book: Book, commands: List[Tuple[str, str]]) -> Optional[str]:
    # Реєстри стратегій (дозволяють легко додавати нові формати)
    formatters: Dict[str, Formatter] = {
        "console": ConsoleFormatter(),
        "reverse": ReverseFormatter()
    }

    serializers: Dict[str, Serializer] = {
        "json": JsonSerializer(),
        "xml": XmlSerializer()
    }

    printer = BookPrinter()
    last_result = None

    for cmd, arg in commands:
        if cmd in ("display", "print"):
            if arg in formatters:
                printer.print_book(book, formatters[arg])
            else:
                raise ValueError(f"Unknown format: {arg}")

        elif cmd == "serialize":
            if arg in serializers:
                last_result = serializers[arg].serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {arg}")

    return last_result
