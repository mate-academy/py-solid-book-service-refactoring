import json
import xml.etree.ElementTree as ET  # noqa: N817
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class DisplayBook(ABC):
    def __init__(self, content: str) -> None:
        self.content = content

    @abstractmethod
    def display(self) -> None:
        pass


class DisplayConsoleBook(DisplayBook):
    def display(self) -> None:
        print(self.content)


class DisplayReverseBook(DisplayBook):
    def display(self) -> None:
        print(self.content[::-1])


def display_book_func(display_type: str, content: str) -> None:
    if display_type == "console":
        DisplayConsoleBook(content).display()
    elif display_type == "reverse":
        DisplayReverseBook(content).display()
    else:
        raise ValueError(f"Unknown display type: {display_type}")


class PrintBook(ABC):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    @abstractmethod
    def print_book(self) -> None:
        pass


class PrintConsoleBook(PrintBook):
    def print_book(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)


class PrintReverseBook(PrintBook):
    def print_book(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])


def print_book_func(print_type: str, title: str, content: str) -> None:
    if print_type == "console":
        PrintConsoleBook(title, content).print_book()
    elif print_type == "reverse":
        PrintReverseBook(title, content).print_book()
    else:
        raise ValueError(f"Unknown print type: {print_type}")


class SerializeBook(ABC):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    @abstractmethod
    def serialize_book(self) -> None:
        pass


class SerializeJsonBook(SerializeBook) :
    def serialize_book(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})


class SerializeXmlBook(SerializeBook):
    def serialize_book(self) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.title
        content = ET.SubElement(root, "content")
        content.text = self.content
        return ET.tostring(root, encoding="unicode")


def serialize_book_func(serialize_type: str, title: str, content: str) -> str:
    if serialize_type == "json":
        return SerializeJsonBook(title, content).serialize_book()
    elif serialize_type == "xml":
        return SerializeXmlBook(title, content).serialize_book()
    else:
        raise ValueError(f"Unknown serialize type: {serialize_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_book_func(method_type, book.content)
        elif cmd == "print":
            print_book_func(method_type, book.title, book.content)
        elif cmd == "serialize":
            return serialize_book_func(method_type, book.title, book.content)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
