import json
from typing import Protocol
import xml.etree.ElementTree as ET


class DisplayStrategy(Protocol):
    def display(self, content: str) -> None:
        ...


class ConsoleDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content[::-1])


class PrintStrategy(Protocol):
    def print(self, title: str, content: str) -> None:
        ...


class ConsolePrint(PrintStrategy):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrint(PrintStrategy):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


class SerializeStrategy(Protocol):
    def serialize(self, title: str, content: str) -> str:
        ...


class JSONSerialize(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XMLSerialize(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        root = ET.Element("book")
        title_elem = ET.SubElement(root, "title")
        title_elem.text = title
        content_elem = ET.SubElement(root, "content")
        content_elem.text = content
        return ET.tostring(root, encoding="unicode")


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def display(self, strategy: DisplayStrategy) -> None:
        strategy.display(self.content)

    def print_book(self, strategy: PrintStrategy) -> None:
        strategy.print(self.title, self.content)

    def serialize(self, strategy: SerializeStrategy) -> str:
        return strategy.serialize(self.title, self.content)


class DisplayHandler:
    strategies = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }

    @staticmethod
    def execute(book: Book, method_type: str) -> None:
        if method_type in DisplayHandler.strategies:
            book.display(DisplayHandler.strategies[method_type])
        else:
            raise ValueError(f"Unknown display method: {method_type}")


class PrintHandler:
    strategies = {
        "console": ConsolePrint(),
        "reverse": ReversePrint(),
    }

    @staticmethod
    def execute(book: Book, method_type: str) -> None:
        if method_type in PrintHandler.strategies:
            book.print_book(PrintHandler.strategies[method_type])
        else:
            raise ValueError(f"Unknown print method: {method_type}")


class SerializeHandler:
    strategies = {
        "json": JSONSerialize(),
        "xml": XMLSerialize(),
    }

    @staticmethod
    def execute(book: Book, method_type: str) -> str:
        if method_type in SerializeHandler.strategies:
            return book.serialize(SerializeHandler.strategies[method_type])
        else:
            raise ValueError(f"Unknown serialize method: {method_type}")
