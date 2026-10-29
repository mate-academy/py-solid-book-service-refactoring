# import json
# import xml.etree.ElementTree as ElementTree
# from abc import ABC, abstractmethod


# class Book:
#     def __init__(self, title: str, content: str) -> None:
#         self.title = title
#         self.content = content


# class Display(ABC):
#     @abstractmethod
#     def display(self, book: Book) -> None:
#         pass


# class ShowBookDetail(ABC):
#     @abstractmethod
#     def show(self, book: Book) -> None:
#         pass
#
#
# class Serializer(ABC):
#     @abstractmethod
#     def serialize(self, book: Book) -> str:
#         pass


# class ConsoleDisplay(Display):
#     def display(self, book: Book) -> None:
#         print(book.content)
#
#
# class ReverseDisplay(Display):
#     def display(self, book: Book) -> None:
#         print(book.content[::-1])
#
#
# class ShowConsoleBookDetail(ShowBookDetail):
#     def show(self, book: Book) -> None:
#         print(f"Printing the book: {book.title}...")
#         print(book.content)
#
#
# class ShowReverseBookDetail(ShowBookDetail):
#     def show(self, book: Book) -> None:
#         print(f"Printing the book in reverse: {book.title}...")
#         print(book.content[::-1])


# class JsonSerialize(Serializer):
#     def serialize(self, book: Book) -> str:
#         return json.dumps({"title": book.title, "content": book.content})
#
#
# class XmlSerialize(Serializer):
#     def serialize(self, book: Book) -> str:
#         root = ElementTree.Element("book")
#         title = ElementTree.SubElement(root, "title")
#         title.text = book.title
#         content = ElementTree.SubElement(root, "content")
#         content.text = book.content
#         return ElementTree.tostring(root, encoding="unicode")

from app.book import Book
from app.displays import (
    ConsoleDisplay,
    ReverseDisplay,
    ShowConsoleBookDetail,
    ShowReverseBookDetail,
)
from app.serializers import JsonSerialize, XmlSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                ConsoleDisplay().display(book)
            elif method_type == "reverse":
                ReverseDisplay().display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            if method_type == "console":
                ShowConsoleBookDetail().show(book)
            elif method_type == "reverse":
                ShowReverseBookDetail().show(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            if method_type == "json":
                return JsonSerialize().serialize(book)
            elif method_type == "xml":
                return XmlSerialize().serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
