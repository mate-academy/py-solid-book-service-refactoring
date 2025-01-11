import json
import xml.etree.ElementTree as ET  # noqa
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class IDisplay(ABC):
    @abstractmethod
    def display(self) -> None:
        pass


class IPrint(ABC):
    @abstractmethod
    def print(self) -> None:
        pass


class ISerialize(ABC):
    @abstractmethod
    def serialize(self) -> str:
        pass


class ConsoleDisplay(IDisplay):
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self) -> None:
        print(self.book.content)


class ReverseDisplay(IDisplay):
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self) -> None:
        print(self.book.content[::-1])


class ConsolePrint(IPrint):
    def __init__(self, book: Book) -> None:
        self.book = book

    def print(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class ReversePrint(IPrint):
    def __init__(self, book: Book) -> None:
        self.book = book

    def print(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])


class JsonSerialize(ISerialize):
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self) -> str:
        return json.dumps(
            {
                "title": self.book.title,
                "content": self.book.content
            }
        )


class XmlSerialize(ISerialize):
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.book.title
        content = ET.SubElement(root, "content")
        content.text = self.book.content
        return ET.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_map = {
        "console": ConsoleDisplay(book),
        "reverse": ReverseDisplay(book)
    }
    print_map = {
        "console": ConsolePrint(book),
        "reverse": ReversePrint(book)
    }
    serialize_map = {
        "json": JsonSerialize(book),
        "xml": XmlSerialize(book)
    }

    for cmd, method_type in commands:
        if cmd == "display":
            display_map[method_type].display()
        elif cmd == "print":
            print_map[method_type].print()
        elif cmd == "serialize":
            return serialize_map[method_type].serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
