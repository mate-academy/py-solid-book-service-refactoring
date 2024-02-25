import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class Displayer(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class ConsoleDisplayer(Displayer):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplayer(Displayer):
    def display(self, content: str) -> None:
        print(content[::-1])


class Printer(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        pass


class ConsolePrinter(Printer):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrinter(Printer):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


class Serializer(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JSONSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XMLSerializer(Serializer):
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

    def display(self, displayer: Displayer) -> None:
        return displayer.display(self.content)

    def print_book(self, printer: Printer) -> None:
        return printer.print_book(self.title, self.content)

    def serialize(self, serializer: Serializer):
        return serializer.serialize(self.title, self.content)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displayer_map = {"console": ConsoleDisplayer(),
                     "reverse": ReverseDisplayer()}
    printer_map = {"console": ConsolePrinter(), "reverse": ReversePrinter()}
    serializer_map = {"json": JSONSerializer(), "xml": XMLSerializer()}
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type in displayer_map:
                book.display(displayer_map[method_type])
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            if method_type in printer_map:
                book.print_book(printer_map[method_type])
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            if method_type in serializer_map:
                return book.serialize(serializer_map[method_type])
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
