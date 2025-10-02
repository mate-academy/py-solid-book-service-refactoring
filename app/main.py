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


def main(
    book: Book, displayer: BookDisplay, printer: BookPrint, serializer: BookSerialize
) -> str:
    displayer.display(book)
    printer.print_book(book)
    return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    reverse_display = ReverseDisplay()
    reverse_print = ReversePrint()
    xml_serialize = XmlSerialize()
    print(main(sample_book, reverse_display, reverse_print, xml_serialize))
