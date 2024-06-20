"""
Dependency Inversion Principle
"""
from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ElTree


class DisplayBook(ABC):
    @abstractmethod
    def display(self, content: str) -> str:
        pass


class PrintBook(ABC):
    @abstractmethod
    def print(self, title: str, content: str) -> str:
        pass


class SerializeBook(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class DisplayConsole(DisplayBook):
    def display(self, content: str) -> None:
        print(content)


class DisplayReverse(DisplayBook):
    def display(self, content: str) -> None:
        print(content[::-1])


class PrintConsole(PrintBook):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class PrintReverse(PrintBook):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


class SerializeToJson(SerializeBook):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class SerializeToXml(SerializeBook):
    def serialize(self, title: str, content: str) -> str:
        root = ElTree.Element("book")
        title_elem = ElTree.SubElement(root, "title")
        title_elem.text = title
        content_elem = ElTree.SubElement(root, "content")
        content_elem.text = content
        return ElTree.tostring(root, encoding="unicode")


class Book:
    def __init__(
            self,
            title: str,
            content: str,
            display_strategy: DisplayBook,
            print_strategy: PrintBook,
            serialize_strategy: SerializeBook
    ) -> None:
        self.title = title
        self.content = content
        self.display_strategy = display_strategy
        self.print_strategy = print_strategy
        self.serialize_strategy = serialize_strategy

    def display(self) -> None:
        self.display_strategy.display(self.content)

    def print_book(self) -> None:
        self.print_strategy.print(self.title, self.content)

    def serialize(self) -> str:
        return self.serialize_strategy.serialize(self.title, self.content)


def main(book: Book, commands: list[str]) -> None | str:
    for cmd in commands:
        if cmd == "display":
            book.display()
        elif cmd == "print":
            book.print_book()
        elif cmd == "serialize":
            return book.serialize()


if __name__ == "__main__":
    display_strategy = DisplayReverse()
    print_strategy = PrintReverse()
    serialize_strategy = SerializeToJson()

    sample_book = Book(
        "Sample Book", "This is some sample content.",
        display_strategy,
        print_strategy,
        serialize_strategy
    )

    print(main(sample_book, ["display", "serialize"]))
