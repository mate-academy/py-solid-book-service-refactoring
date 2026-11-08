import json
from abc import ABC, abstractmethod
from xml.etree import ElementTree


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


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


class BookManager:
    def __init__(self, book: Book) -> None:
        self.book = book
        self._display_strategies = {
            "console": ConsoleDisplay(),
            "reverse": ReverseDisplay(),
        }
        self._print_strategies = {
            "console": ConsolePrint(),
            "reverse": ReversePrint(),
        }
        self._serializers = {
            "json": JsonSerializer(),
            "xml": XmlSerializer(),
        }

    def display(self, method_type: str) -> None:
        strategy = self._display_strategies.get(method_type)
        if not strategy:
            raise ValueError(f"Unknown display type: {method_type}")
        strategy.display(self.book)

    def print_book(self, method_type: str) -> None:
        strategy = self._print_strategies.get(method_type)
        if not strategy:
            raise ValueError(f"Unknown print type: {method_type}")
        strategy.print_book(self.book)

    def serialize(self, serialize_type: str) -> str:
        strategy = self._serializers.get(serialize_type)
        if not strategy:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
        return strategy.serialize(self.book)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    manager = BookManager(book)
    for cmd, method_type in commands:
        if cmd == "display":
            manager.display(method_type)
        elif cmd == "print":
            manager.print_book(method_type)
        elif cmd == "serialize":
            return manager.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
