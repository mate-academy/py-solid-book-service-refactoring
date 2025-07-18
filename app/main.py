import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


# Abstract book interfaces
class BookDisplayInterface(ABC):
    @abstractmethod
    def display(self, content: str): pass


class BookPrintInterface(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str): pass


class BookSerializeInterface(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str: pass


# Concrete implementations for different book-related actions
class DisplayConsole(BookDisplayInterface):
    def display(self, content: str) -> None:
        print(content)


class DisplayReverse(BookDisplayInterface):
    def display(self, content: str) -> None:
        print(content[::-1])


class PrintConsole(BookPrintInterface):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class PrintReverse(BookPrintInterface):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


class SerializeJson(BookSerializeInterface):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class SerializeXml(BookSerializeInterface):
    def serialize(self, title: str, content: str) -> str:
        root = ET.Element("book")
        title_elem = ET.SubElement(root, "title")
        title_elem.text = title
        content_elem = ET.SubElement(root, "content")
        content_elem.text = content
        return ET.tostring(root, encoding="unicode")


# Dictionaries mapping strategy names to their respective classes (used as factories)
DISPLAY_STRATEGIES: dict[str, type[BookDisplayInterface]] = {
    "console": DisplayConsole,
    "reverse": DisplayReverse
}

PRINT_STRATEGIES: dict[str, type[BookPrintInterface]] = {
    "console": PrintConsole,
    "reverse": PrintReverse
}

SERIALIZE_STRATEGIES: dict[str, type[BookSerializeInterface]] = {
    "json": SerializeJson,
    "xml": SerializeXml
}


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def display(self, interface: BookDisplayInterface) -> None:
        interface.display(self.content)

    def print_book(self, interface: BookPrintInterface) -> None:
        interface.print_book(self.title, self.content)

    def serialize(self, strategy: BookSerializeInterface) -> str:
        return strategy.serialize(self.title, self.content)


# Functions for process book strategies
def get_display_strategy(name: str) -> BookDisplayInterface:
    try:
        return DISPLAY_STRATEGIES[name]()
    except KeyError:
        raise ValueError(f"Unknown display strategy: {name}")


def get_print_strategy(name: str) -> BookPrintInterface:
    try:
        return PRINT_STRATEGIES[name]()
    except KeyError:
        raise ValueError(f"Unknown print strategy: {name}")


def get_serialize_strategy(name: str) -> BookSerializeInterface:
    try:
        return SERIALIZE_STRATEGIES[name]()
    except KeyError:
        raise ValueError(f"Unknown serialize strategy: {name}")


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(get_display_strategy(method_type))
        elif cmd == "print":
            book.print_book(get_print_strategy(method_type))
        elif cmd == "serialize":
            return book.serialize(get_serialize_strategy(method_type))
        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
