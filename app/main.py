import json
import xml.etree.ElementTree as ET
from typing import Callable


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

class Serializer:
    def __init__(self, book):
        self.book = book

    def json_serialize(self):
        return json.dumps({"title": self.book.title, "content": self.book.content})

    def xml_serialize(self):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.book.title
        content = ET.SubElement(root, "content")
        content.text = self.book.content
        return ET.tostring(root, encoding="unicode")

    def serialize(self, method_type: str):
        method_name = f"{method_type}_serialize"
        method = getattr(self, method_name, None)

        if not callable(method):
            raise ValueError(f"Unknown display method: {method_type}")

        return method()


class Displayer:
    def __init__(self, book):
        self.book = book

    def display_console(self):
        print(self.book.content)

    def display_reverse(self):
        print(self.book.content[::-1])

    def display(self, method_type: str):
        method_name = f"display_{method_type}"
        method = getattr(self, method_name, None)

        if not callable(method):
            raise ValueError(f"Unknown display method: {method_type}")

        method()


class Printer:
    def __init__(self, book):
        self.book = book

    def print_console(self):
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)

    def print_reverse(self):
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])

    def print_content(self, method_type: str):
        method_name = f"print_{method_type}"
        method = getattr(self, method_name, None)

        if not callable(method):
            raise ValueError(f"Unknown print type: {method_type}")

        method()


def main(book: Book, commands: list[tuple[str, str]]) -> None | str | Callable:
    for cmd, method_type in commands:
        if cmd == "display":
            display = Displayer(book)
            display.display(method_type)
        elif cmd == "print":
            to_print = Printer(book)
            to_print.print_content(method_type)
        elif cmd == "serialize":
            to_serialize = Serializer(book)
            return to_serialize.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("print", "reverse"), ("serialize", "xml")]))
