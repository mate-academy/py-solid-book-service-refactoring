import json

import xml.etree.ElementTree as XmlET

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


class ReverseConsoleDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content[::-1])


class PrintStrategy(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        pass


class ConsolePrint(PrintStrategy):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...", content)


class ReverseConsolePrint(PrintStrategy):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...", content[::-1])


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerialize(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerialize(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        root = XmlET.Element("book")
        title = XmlET.SubElement(root, "title")
        title.text = book.title
        content = XmlET.SubElement(root, "content")
        content.text = book.content
        return XmlET.tostring(root, encoding="unicode")


class BookProcessor:
    def __init__(
            self,
            book: Book,
            display_strategy: DisplayStrategy,
            print_strategy: PrintStrategy,
            serialize_strategy: SerializeStrategy
    ) -> None:

        self.book = book
        self.display_strategy = display_strategy
        self.print_strategy = print_strategy
        self.serialize_strategy = serialize_strategy

    def display(self) -> None:
        self.display_strategy.display(self.book.content)

    def print_book(self) -> None:
        self.print_strategy.print_book(self.book.title, self.book.content)

    def serialize(self) -> str:
        return self.serialize_strategy.serialize(self.book)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_strategy = ConsoleDisplay()
    print_strategy = ConsolePrint()
    serialize_strategy = JsonSerialize()
    bp = BookProcessor(
        book,
        display_strategy,
        print_strategy,
        serialize_strategy
    )
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "reverse":
                bp.display_strategy = ReverseConsoleDisplay()
            else:
                bp.display_strategy = ConsoleDisplay()

            bp.display()

        elif cmd == "print":
            if method_type == "reverse":
                bp.print_strategy = ReverseConsolePrint()
            else:
                bp.print_strategy = ConsolePrint()

            bp.print_book()

        elif cmd == "serialize":
            if method_type == "xml":
                bp.serialize_strategy = XmlSerialize()
            else:
                bp.serialize_strategy = JsonSerialize()

            return bp.serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
