import json
import xml.etree.ElementTree as Et
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.__title = title
        self.__content = content

    @property
    def title(self) -> str:
        return self.__title

    @property
    def content(self) -> str:
        return self.__content


class Display(ABC):

    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(Display):

    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(Display):

    def display(self, book: Book) -> None:
        print(book.content[::-1])


class Print(ABC):

    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrint(Print):

    def print_book(self, book: Book) -> None:
        print(
            f"Printing the book: {book.title}..."
            f"{book.content}"
        )


class ReversePrint(Print):

    def print_book(self, book: Book) -> None:
        print(
            f"Printing the book in reverse: {book.title}..."
            f"{book.content[::-1]}"
        )


class Serializer(ABC):

    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONSerializer(Serializer):

    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(Serializer):

    def serialize(self, book: Book) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = book.title
        content = Et.SubElement(root, "content")
        content.text = book.content
        return Et.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                book_display = ConsoleDisplay()
            elif method_type == "reverse":
                book_display = ReverseDisplay()
            else:
                raise ValueError(f"Unknown display type: {method_type}")
            book_display.display(book)
        elif cmd == "print":
            if method_type == "console":
                book_print = ConsolePrint()
            elif method_type == "reverse":
                book_print = ReversePrint()
            else:
                raise ValueError(f"Unknown print type: {method_type}")
            book_print.print_book(book)
        elif cmd == "serialize":
            if method_type == "json":
                serialize_book = JSONSerializer()
            elif method_type == "xml":
                serialize_book = XMLSerializer()
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serialize_book.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
