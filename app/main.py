import json
import xml.etree.ElementTree as ETree
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class DisplayBook(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class DisplayConsoleBook(DisplayBook):
    def display(self, book: Book) -> None:
        print(book.content)


class DisplayReverseBook(DisplayBook):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class PrintBook(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class PrintConsoleBook(PrintBook):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintReverseBook(PrintBook):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class SerializeBook(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class SerializeJSONBook(SerializeBook):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeXMLBook(SerializeBook):
    def serialize(self, book: Book) -> str:
        root = ETree.Element("book")
        title = ETree.SubElement(root, "title")
        title.text = book.title
        content = ETree.SubElement(root, "content")
        content.text = book.content
        return ETree.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display = {
        "console": DisplayConsoleBook(),
        "reverse": DisplayReverseBook()
    }

    print_book = {
        "console": PrintConsoleBook(),
        "reverse": PrintReverseBook()
    }

    serialize = {
        "json": SerializeJSONBook(),
        "xml": SerializeXMLBook()
    }

    for cmd, method_type in commands:
        if cmd == "display":
            displayer = display.get(method_type)
            if displayer:
                displayer.display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")

        elif cmd == "print":
            printer = print_book.get(method_type)
            if printer:
                printer.print_book(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")

        elif cmd == "serialize":
            serializer = serialize.get(method_type)
            if serializer:
                return serializer.serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
