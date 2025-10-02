import json
import xml.etree.ElementTree
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class BookDisplay(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class BookPrint(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class BookSerialize(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class ConsoleDisplay(BookDisplay):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(BookDisplay):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class ConsolePrint(BookPrint):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(BookPrint):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class JsonSerialize(BookSerialize):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerialize(BookSerialize):
    def serialize(self, book: Book) -> str:
        root = xml.etree.ElementTree.Element("book")
        title = xml.etree.ElementTree.SubElement(root, "title")
        title.text = book.title
        content = xml.etree.ElementTree.SubElement(root, "content")
        content.text = book.content
        return xml.etree.ElementTree.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displayers = {
        "console": ConsoleDisplay,
        "reverse": ReverseDisplay,
    }
    printers = {
        "console": ConsolePrint,
        "reverse": ReversePrint,
    }
    serializers = {
        "json": JsonSerialize,
        "xml": XmlSerialize,
    }

    result = None

    for cmd, method_type in commands:
        if cmd == "display":
            displayer = displayers.get(method_type)
            if displayer is None:
                raise ValueError(f"Unknown display type: {method_type}")
            displayer().display(book)

        elif cmd == "print":
            printer = printers.get(method_type)
            if printer is None:
                raise ValueError(f"Unknown print type: {method_type}")
            printer().print_book(book)

        elif cmd == "serialize":
            serializer = serializers.get(method_type)
            if serializer is None:
                raise ValueError(f"Unknown serialize type: {method_type}")
            result = serializer().serialize(book)

        else:
            raise ValueError(f"Unknown command: {cmd}")

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
