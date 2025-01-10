import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayStrategy):
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
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


class Printer:
    def print_book(
            self,
            book: Book,
            display_strategy: DisplayStrategy
    ) -> None:
        print(f"Printing the book: {book.title}...")
        display_strategy.display(book)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    serializers = {"json": JSONSerializer(), "xml": XMLSerializer()}
    displays = {"console": ConsoleDisplay(), "reverse": ReverseDisplay()}

    for cmd, method_type in commands:
        if cmd == "display":
            if method_type in displays:
                displays[method_type].display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            if method_type in displays:
                Printer().print_book(book, displays[method_type])
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            if method_type in serializers:
                return serializers[method_type].serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
