import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str):
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


class PrintStrategy(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrint(PrintStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(PrintStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


class BookManager:
    display_strategies = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }

    print_strategies = {
        "console": ConsolePrint(),
        "reverse": ReversePrint(),
    }

    serialize_strategies = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }

    def __init__(self, book: Book):
        self.book = book

    def execute(self, command: str, method: str) -> str | None:
        if command == "display":
            strategy = self.display_strategies.get(method)
            if not strategy:
                raise ValueError(f"Unknown display type: {method}")
            strategy.display(self.book)

        elif command == "print":
            strategy = self.print_strategies.get(method)
            if not strategy:
                raise ValueError(f"Unknown print type: {method}")
            strategy.print_book(self.book)

        elif command == "serialize":
            strategy = self.serialize_strategies.get(method)
            if not strategy:
                raise ValueError(f"Unknown serialize type: {method}")
            return strategy.serialize(self.book)

        else:
            raise ValueError(f"Unknown command: {command}")


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    manager = BookManager(book)
    result = None
    for cmd, method in commands:
        res = manager.execute(cmd, method)
        if res:
            result = res
    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
