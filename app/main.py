import json
import xml.etree.ElementTree
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class DisplayBook(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(DisplayBook):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayBook):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class SerializeBook(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerialize(SerializeBook):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerialize(SerializeBook):
    def serialize(self, book: Book) -> str:
        root = xml.etree.ElementTree.Element("book")
        title = xml.etree.ElementTree.SubElement(root, "title")
        title.text = book.title
        content = xml.etree.ElementTree.SubElement(root, "content")
        content.text = book.content
        return xml.etree.ElementTree.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                ConsoleDisplay().display(book)
            elif method_type == "reverse":
                ReverseDisplay().display(book)
        elif cmd == "print":
            print(book.title)
            if method_type == "console":
                print(book.content)
            elif method_type == "reverse":
                print(book.content[::-1])
        elif cmd == "serialize":
            if method_type == "json":
                return JsonSerialize().serialize(book)
            elif method_type == "xml":
                return XmlSerialize().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
