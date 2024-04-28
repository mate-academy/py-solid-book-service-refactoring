from __future__ import annotations

import json
import xml.etree.ElementTree as Et
from abc import ABC


class Base(ABC):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, *args, **kwargs) -> None:
        pass


class Book(Base):
    def __init__(self, title: str, content: str) -> None:
        super().__init__(title, content)

    def display(self, *args, **kwargs) -> None:
        pass


class Json(Base):
    def __init__(self, title, content):
        super().__init__(title, content)

    def display(self):
        return json.dumps({"title": self.title, "content": self.content})


class XML(Base):
    def __init__(self, title, content):
        super().__init__(title, content)

    def display(self):
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = self.title
        content = Et.SubElement(root, "content")
        content.text = self.content
        return Et.tostring(root, encoding="unicode")


class Serializer(Base):

    def __init__(self, title, content):
        super().__init__(title, content)

    def display(self, serialize_type: str) -> Et | json:
        if serialize_type == "json":
            return Json(self.title, self.content).display()
        elif serialize_type == "xml":
            return XML(self.title, self.content).display()
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")


class Console(Book):
    def __init__(self, title, content):
        super().__init__(title, content)

    def print_with_title(self):
        print(f"Printing the book: {self.title}...")
        print(self.content)

    def print_without_title(self):
        print(self.content)


class Reverse(Book):
    def __init__(self, title, content):
        super().__init__(title, content)

    def print_with_title(self):
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])

    def print_without_title(self):
        print(self.content[::-1])


class Print(Book):
    def __init__(self, title: str, content: str) -> None:
        super().__init__(title, content)

    def display(self, print_type: str) -> None:
        if print_type == "console":
            Console(self.title, self.content).print_with_title()
        elif print_type == "reverse":
            Reverse(self.title, self.content).print_with_title()
        else:
            raise ValueError(f"Unknown print type: {print_type}")


class Display(Book):
    def __init__(self, title: str, content: str) -> None:
        super().__init__(title, content)

    def display(self, display_type: str) -> None:
        if display_type == "console":
            Console(self.title, self.content).print_without_title()
        elif display_type == "reverse":
            Reverse(self.title, self.content).print_without_title()
        else:
            raise ValueError(f"Unknown display type: {display_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book = Display(book.title, book.content)
            book.display(method_type)
        elif cmd == "print":
            book = Print(book.title, book.content)
            book.display(method_type)
        elif cmd == "serialize":
            book = Serializer(book.title, book.content)
            return book.display(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
