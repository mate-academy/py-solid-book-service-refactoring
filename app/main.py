import json

import xml.etree.ElementTree as ETree
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
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


class Printer(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrinter(Printer):

    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(Printer):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class Serialize(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class JsonSerialize(Serialize):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerialize(Serialize):
    def serialize(self, book: Book) -> str:
        root = ETree.Element("book")
        title = ETree.SubElement(root, "title")
        title.text = book.title
        content = ETree.SubElement(root, "content")
        content.text = book.content
        return ETree.tostring(root, encoding="unicode")


class Command(ABC):
    @abstractmethod
    def execute(self, book: Book) -> None:
        pass


class DisplayCommand(Command):
    def __init__(self, display: ConsoleDisplay | ReverseDisplay) -> None:
        self.display = display

    def execute(self, book: Book) -> None:
        self.display.display(book)


class PrintCommand(Command):
    def __init__(self, printer: ConsolePrinter | ReversePrinter) -> None:
        self.printer = printer

    def execute(self, book: Book) -> None:
        self.printer.print_book(book)


class SerializeCommand(Command):
    def __init__(self, serialize: JsonSerialize | XmlSerialize) -> None:
        self.serialize = serialize

    def execute(self, book: Book) -> str:
        return self.serialize.serialize(book)


class CommandFactory:
    @staticmethod
    def create(
            cmd: str,
            method_type: str
    ) -> DisplayCommand | PrintCommand | SerializeCommand:
        if cmd == "display":
            display = {
                "console": ConsoleDisplay(),
                "reverse": ReverseDisplay()
            }
            return DisplayCommand(display[method_type])
        elif cmd == "print":
            printers = {
                "console": ConsolePrinter(),
                "reverse": ReversePrinter()
            }
            return PrintCommand(printers[method_type])
        elif cmd == "serialize":
            serialize = {
                "json": JsonSerialize(),
                "xml": XmlSerialize()
            }
            return SerializeCommand(serialize[method_type])
        raise ValueError(f"Unknown command: {cmd}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        command = CommandFactory.create(cmd, method_type)
        result = command.execute(book)
        if result is not None:
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
