import json
import xml.etree.ElementTree as ET

from app.displays import Display, ConsoleDisplay, ReverseDisplay
from app.print_classes import AbstractPrint, ConsolePrint, ReversePrint
from app.serializers import Serializer, JsonSerializer, XmlSerializer


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def display(self, display: Display) -> None:
        print(display.display(self.content))

    def print_book(self, print_type: AbstractPrint) -> None:
        print_type.print(self.title, self.content)

    def serialize(self, serialize_type: Serializer) -> str:
        return serialize_type.serialize(self.title, self.content)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                book.display(ConsoleDisplay())
            if method_type == "reverse":
                book.display(ReverseDisplay())
        elif cmd == "print":
            if method_type == "console":
                book.print_book(ConsolePrint())
            if method_type == "reverse":
                book.print_book(ReversePrint())
        elif cmd == "serialize":
            if method_type == "json":
                return book.serialize(JsonSerializer())
            if method_type == "xml":
                return book.serialize(XmlSerializer())


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
