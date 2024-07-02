import json
import xml.etree.ElementTree as ET  # noqa: N817
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class ConsoleDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content[::-1])


class PrintStrategy(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        pass


class ConsolePrint(PrintStrategy):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}\n{content}")


class ReversePrint(PrintStrategy):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...\n{content[::-1]}")


class SerializerStrategy(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerialize(SerializerStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(SerializerStrategy):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


class BookService:
    def __init__(self) -> None:
        self.display_strategy: DisplayStrategy | None = None
        self.print_strategy: PrintStrategy | None = None
        self.serializer_strategy: SerializerStrategy | None = None

    def set_display_strategy(self, strategy: DisplayStrategy) -> None:
        self.display_strategy = strategy

    def set_print_strategy(self, strategy: PrintStrategy) -> None:
        self.print_strategy = strategy

    def set_serializer_strategy(self, strategy: SerializerStrategy) -> None:
        self.serializer_strategy = strategy

    def display(self, book: Book) -> None:
        if self.display_strategy:
            self.display_strategy.display(book.content)

    def print_book(self, book: Book) -> None:
        if self.print_strategy:
            self.print_strategy.print_book(book.title, book.content)

    def serialize(self, book: Book) -> str:
        if self.serializer_strategy:
            return self.serializer_strategy.serialize(book)
        return ""


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    book_service = BookService()
    result = None

    display_strategies = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }

    print_strategies = {"console": ConsolePrint(), "reverse": ReversePrint()}

    serialize_strategies = {"json": JsonSerialize(), "xml": XMLSerializer()}

    for cmd, method_type in commands:
        if cmd == "display" and method_type in display_strategies:
            book_service.set_display_strategy(display_strategies[method_type])
            book_service.display(book)
        elif cmd == "print" and method_type in print_strategies:
            book_service.set_print_strategy(print_strategies[method_type])
            book_service.print_book(book)
        elif cmd == "serialize" and method_type in serialize_strategies:
            book_service.set_serializer_strategy(
                serialize_strategies[method_type]
            )
            result = book_service.serialize(book)
        else:
            raise ValueError(
                f"Unknown command or strategy:"
                f" {cmd} with method type: {method_type}"
            )

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
