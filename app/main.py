import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod


# Book
class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


# Display
class Display(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class DisplayConsole(Display):
    def display(self, book: Book) -> None:
        print(book.content)


class DisplayReverse(Display):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


# Print
class Printer(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class PrintConsole(Printer):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintReverse(Printer):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


# Serialize
class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class SerializeJSON(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeXML(Serializer):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        ElementTree.SubElement(root, "title").text = book.title
        ElementTree.SubElement(root, "content").text = book.content
        return ElementTree.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display = DisplayConsole() if method_type == "console"\
                else DisplayReverse()
            display.display(book)
        elif cmd == "print":
            printer = PrintConsole() if method_type == "console"\
                else PrintReverse()
            printer.print(book)
        elif cmd == "serialize":
            serializer = SerializeJSON() if method_type == "json"\
                else SerializeXML()
            return serializer.serialize(book)
        else:
            raise ValueError(f"Unknown command {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
