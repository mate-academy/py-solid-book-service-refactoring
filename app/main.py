import json
import xml.etree.ElementTree as Et
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


class PrintStrategy(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class ConsolePrint(PrintStrategy):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(PrintStrategy):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class SerializerStrategy(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(SerializerStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(SerializerStrategy):
    def serialize(self, book: Book) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = book.title
        content = Et.SubElement(root, "content")
        content.text = book.content
        return Et.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    display_strategies = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }

    print_strategies = {
        "console": ConsolePrint(),
        "reverse": ReversePrint(),
    }

    serializer_strategies = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }

    result = None

    for command, method_type in commands:
        if command == "display":
            strategy = display_strategies.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown display type: {method_type}")
            strategy.display(book)

        elif command == "print":
            strategy = print_strategies.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown print type: {method_type}")
            strategy.print(book)

        elif command == "serialize":
            strategy = serializer_strategies.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown serialize type: {method_type}")
            result = strategy.serialize(book)

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
