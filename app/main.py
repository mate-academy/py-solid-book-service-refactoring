import json
import xml.etree.ElementTree as Et
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class Display(ABC):
    def __init__(self, book: Book, display_type: str) -> None:
        self.display_type = display_type
        self.book = book

    @abstractmethod
    def display(self) -> None:
        pass


class DisplayConsole(Display):
    def display(self) -> None:
        print(self.book.content)


class DisplayReverse(Display):
    def display(self) -> None:
        print(self.book.content[::-1])


class DisplayError(Display):
    def display(self) -> None:
        raise ValueError(f"Unknown display type: {self.display_type}")


class PrintBook(ABC):
    def __init__(self, book: Book, print_type: str) -> None:
        self.print_type = print_type
        self.book = book

    @abstractmethod
    def print_book(self) -> None:
        pass


class PrintBookConsole(PrintBook):
    def print_book(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class PrintBookReverse(PrintBook):
    def print_book(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])


class PrintBookError(PrintBook):
    def print_book(self) -> None:
        raise ValueError(f"Unknown print type: {self.print_type}")


class Serialize(ABC):
    def __init__(self, book: Book, serialize_type: str) -> None:
        self.serialize_type = serialize_type
        self.book = book

    @abstractmethod
    def serialize(self) -> str:
        pass


class SerializeJson(Serialize):
    def serialize(self) -> str:
        return json.dumps(
            {"title": self.book.title, "content": self.book.content}
        )


class SerializeXml(Serialize):
    def serialize(self) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = self.book.title
        content = Et.SubElement(root, "content")
        content.text = self.book.content
        return Et.tostring(root, encoding="unicode")


class SerializeError(Serialize):
    def serialize(self) -> str:
        raise ValueError(f"Unknown serialize type: {self.serialize_type}")


def display(book: Book, method_type: str) -> None:
    match method_type:
        case "console":
            display_console = DisplayConsole(book, method_type)
            display_console.display()
        case "reverse":
            display_reverse = DisplayReverse(book, method_type)
            display_reverse.display()
        case None:
            display_error = DisplayError(book, method_type)
            display_error.display()


def print_book(book: Book, method_type: str) -> None:
    match method_type:
        case "console":
            print_book_console = PrintBookConsole(book, method_type)
            print_book_console.print_book()
        case "reverse":
            print_book_console = PrintBookReverse(book, method_type)
            print_book_console.print_book()
        case None:
            print_book_console = PrintBookError(book, method_type)
            print_book_console.print_book()


def serialize(book: Book, method_type: str) -> None | str:
    match method_type:
        case "json":
            serialize_json = SerializeJson(book, method_type)
            return serialize_json.serialize()
        case "xml":
            serialize_xml = SerializeXml(book, method_type)
            return serialize_xml.serialize()
        case None:
            serialize_error = SerializeError(book, method_type)
            return serialize_error.serialize()


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display(book, method_type)
        elif cmd == "print":
            print_book(book, method_type)
        elif cmd == "serialize":
            return serialize(book, method_type)



if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
