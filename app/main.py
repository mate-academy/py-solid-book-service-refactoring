import json
import xml.etree.ElementTree as ETree
from abc import ABC, abstractmethod
from app.utils import execute_strategy


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


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        root = ETree.Element("book")
        ETree.SubElement(root, "title").text = book.title
        ETree.SubElement(root, "content").text = book.content
        return ETree.tostring(root, encoding="unicode")


def main(
        book: Book,
        commands: list[tuple[str, str]]
) -> list[str | None] | None:
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

    results = []

    for cmd, method_type in commands:
        if cmd == "display":
            execute_strategy(display_strategies, method_type, book, "display")
            results.append(None)

        elif cmd == "print":
            execute_strategy(print_strategies, method_type, book, "print")
            results.append(None)

        elif cmd == "serialize":
            result = execute_strategy(
                serialize_strategies, method_type, book, "serialize"
            )
            results.append(result)

        else:
            raise ValueError(f"Unknown command: {cmd}")

    if len(results) == 1:
        return results[0]
    return results


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
