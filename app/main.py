import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod
from typing import Any


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class Display(ABC):
    @abstractmethod
    def render(self, book: Book) -> None:
        ...


class ConsoleDisplay(Display):
    def render(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(Display):
    def render(self, book: Book) -> None:
        print(book.content[::-1])


class Print(ABC):
    @abstractmethod
    def do_print(self, book: Book) -> None:
        pass


class ConsolePrint(Print):
    def do_print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(Print):
    def do_print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, Any]]) -> None:
    result = ""
    render_display = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }

    render_print = {
        "console": ConsolePrint(),
        "reverse": ReversePrint(),
    }

    render_serializer = {
        "xml": XmlSerializer(),
        "json": JsonSerializer(),
    }

    for action, executor in commands:
        if action == "display":
            display = render_display.get(executor)
            if display:
                display.render(book)
            else:
                raise ValueError(f"Unknown display type: {executor}")

        elif action == "print":
            printer = render_print.get(executor)
            if printer:
                printer.do_print(book)
            else:
                raise ValueError(f"Unknown print type: {executor}")

        elif action == "serialize":
            serializer = render_serializer.get(executor)
            if serializer:
                result += serializer.serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {executor}")

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
