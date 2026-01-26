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


class ReverseDisplay(Display):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class ConsoleDisplay(Display):
    def display(self, book: Book) -> None:
        print(book.content)


class Print(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class PrintReverse(Print):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class PrintConsole(Print):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class Serialize(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class XmlSerialize(Serialize):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


class JsonSerialize(Serialize):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class Command(ABC):
    @abstractmethod
    def execute(self) -> None | str:
        pass


class DisplayCommand(Command):
    def __init__(self, display: Display, book: Book):
        self.display = display
        self.book = book

    def execute(self):
        self.display.display(self.book)


class PrintCommand(Command):
    def __init__(self, printer: Print, book: Book):
        self.printer = printer
        self.book = book

    def execute(self):
        self.printer.print_book(self.book)


class SerializeCommand(Command):
    def __init__(self, serializer: Serialize, book: Book):
        self.serializer = serializer
        self.book = book

    def execute(self):
        return self.serializer.serialize(self.book)


def main(commands: list[Command]) -> None | str:
    for cmd in commands:
        result = cmd.execute()
        if result is not None:
            return result


if __name__ == "__main__":
    book = Book("Sample Book", "This is some sample content.")

    commands: list[Command] = [
        DisplayCommand(ConsoleDisplay(), book),
        DisplayCommand(ReverseDisplay(), book),
        SerializeCommand(XmlSerialize(), book),
    ]

    print(main(commands))
