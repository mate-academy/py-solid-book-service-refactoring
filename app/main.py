import json
from xml.etree import ElementTree
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class BookCommand:
    def __init__(self, book: Book) -> None:
        self.book = book


class BookDisplay(ABC):
    @abstractmethod
    def display(self) -> None:
        pass


class BookPrinter(ABC):
    @abstractmethod
    def print_book(self) -> None:
        pass


class BookSerialize(ABC):
    @staticmethod
    @abstractmethod
    def serialize(book: Book) -> None:
        pass


class BookConsole(BookDisplay, BookPrinter, BookCommand):
    def display(self) -> None:
        print(self.book.content)

    def print_book(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class BookReverse(BookDisplay, BookPrinter, BookCommand):
    def display(self) -> None:
        print(self.book.content[::-1])

    def print_book(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])


class BookSerializeJSON(BookSerialize):
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class BookSerializeXML(BookSerialize):
    @staticmethod
    def serialize(book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    _book = None
    for cmd, method_type in commands:
        if method_type == "console":
            _book = BookConsole(book)
        elif method_type == "reverse":
            _book = BookReverse(book)
        elif method_type == "xml" and cmd == "serialize":
            return BookSerializeXML.serialize(book)
        elif method_type == "json" and cmd == "serialize":
            return BookSerializeJSON.serialize(book)
        else:
            return "No such method type"
        if cmd == "display":
            _book.display()
        elif cmd == "print":
            _book.print_book()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
