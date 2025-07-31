import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class PrintStrategy(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrint(PrintStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(PrintStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerialize(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerialize(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


class BookService:
    def __init__(self, book: Book):
        self.book = book

    def display(self, display_type: str) -> None:
        if display_type == "console":
            ConsoleDisplay().display(self.book)
        elif display_type == "reverse":
            ReverseDisplay().display(self.book)
        else:
            raise ValueError(f"Unknown display type: {display_type}")

    def print_book(self, print_type: str) -> None:
        if print_type == "console":
            ConsolePrint().print_book(self.book)
        elif print_type == "reverse":
            ReversePrint().print_book(self.book)
        else:
            raise ValueError(f"Unknown print type: {print_type}")

    def serialize(self, serialize_type: str) -> str:
        if serialize_type == "json":
            return JsonSerialize().serialize(self.book)
        elif serialize_type == "xml":
            return XmlSerialize().serialize(self.book)
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    service = BookService(book)
    for cmd, method_type in commands:
        if cmd == "display":
            service.display(method_type)
        elif cmd == "print":
            service.print_book(method_type)
        elif cmd == "serialize":
            return service.serialize(method_type)
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))