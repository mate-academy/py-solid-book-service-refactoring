import json
import xml.etree.ElementTree as ElT
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


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = ElT.Element("book")
        title = ElT.SubElement(root, "title")
        title.text = book.title
        content = ElT.SubElement(root, "content")
        content.text = book.content
        return ElT.tostring(root, encoding="unicode")


def main(book: Book, actions: list) -> None or str:
    actions_dict = {
        "display": {"console": ConsoleDisplay, "reverse": ReverseDisplay},
        "print": {
            "console": (book.title, book.content),
            "reverse": (book.title, book.content[::-1])
        },
        "serialize": {"json": JSONSerializer, "xml": XMLSerializer},
    }
    for action, method in actions:
        if action == "display":
            actions_dict[action][method]().display(book)
        if action == "print":
            print(actions_dict[action][method])
        if action == "serialize":
            return actions_dict[action][method]().serialize(book)


if __name__ == "__main__":
    book = Book("Sample Book", "This is some sample content.")
    actions = [
        ("display", "console"),
        ("display", "reverse"),
        ("print", "console"),
        ("print", "reverse"),
        ("serialize", "json"),
        ("serialize", "xml"),
    ]
    main(book, actions)
