import json
from xml.etree import ElementTree
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


class SerializationStrategy(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(SerializationStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(SerializationStrategy):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


DISPLAY_STRATEGIES = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}

PRINT_STRATEGIES = {
    "console": ConsolePrint(),
    "reverse": ReversePrint(),
}

SERIALIZE_STRATEGIES = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            strategy = DISPLAY_STRATEGIES.get(method_type)
            if strategy:
                strategy.display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")

        elif cmd == "print":
            strategy = PRINT_STRATEGIES.get(method_type)
            if strategy:
                strategy.print_book(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")

        elif cmd == "serialize":
            strategy = SERIALIZE_STRATEGIES.get(method_type)
            if strategy:
                return strategy.serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
