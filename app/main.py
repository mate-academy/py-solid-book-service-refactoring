import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class BookDisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(BookDisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(BookDisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class BookPrintStrategy(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrinter(BookPrintStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(BookPrintStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title_elem = ElementTree.SubElement(root, "title")
        title_elem.text = book.title
        content_elem = ElementTree.SubElement(root, "content")
        content_elem.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    result: None | str = None
    for command, method_type in commands:
        if command == "display":
            display_strategy: BookDisplayStrategy = (
                ConsoleDisplay() if method_type == "console"
                else ReverseDisplay()
            )
            display_strategy.display(book)
        elif command == "print":
            print_strategy: BookPrintStrategy = (
                ConsolePrinter() if method_type == "console"
                else ReversePrinter()
            )
            print_strategy.print_book(book)
        elif command == "serialize":
            serializer: BookSerializer = (
                JsonSerializer() if method_type == "json" else XmlSerializer()
            )
            result = serializer.serialize(book)
    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    output = main(sample_book, [("display", "reverse"), ("serialize", "xml")])
    if output:
        print(output)
