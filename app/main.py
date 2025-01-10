import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


class Display(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(Display):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(Display):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


def displayer(display_type: str, book: Book) -> None:
    if display_type == "console":
        display_instance = ConsoleDisplay()
    elif display_type == "reverse":
        display_instance = ReverseDisplay()
    else:
        raise ValueError(f"Unknown display type: {display_type}")

    display_instance.display(book)


class Print(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class ConsolePrint(Print):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)

class ReversePrint(Print):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


def printer(print_type: str, book: Book) -> None:
    if print_type == "console":
        print_instance = ConsolePrint()
    elif print_type == "reverse":
        print_instance = ReversePrint()
    else:
        raise ValueError(f"Unknown display type: {print_type}")

    print_instance.print(book)


class Serialize(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class JsonSerialize(Serialize):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerialize(Serialize):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


def serializer(serialize_type: str, book: Book) -> str:
    if serialize_type == "json":
        serialize_instance = JsonSerialize()
    elif serialize_type == "xml":
        serialize_instance = XMLSerialize()
    else:
        raise ValueError(f"Unknown serialize type: {serialize_type}")

    return serialize_instance.serialize(book)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            displayer(method_type, book)
        elif cmd == "print":
            printer(method_type, book)
        elif cmd == "serialize":
            return serializer(method_type, book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
