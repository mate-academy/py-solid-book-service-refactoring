import json
import xml.etree.ElementTree as ET # noqa
from typing import Protocol


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class IDisplayProcessor(Protocol):
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplayProcessor:
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplayProcessor:
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class DisplayFactory:
    @staticmethod
    def get(display_type: str) -> IDisplayProcessor:
        match display_type:
            case "console":
                return ConsoleDisplayProcessor()
            case "reverse":
                return ReverseDisplayProcessor()
            case _:
                raise ValueError(f"Unknown display type: {display_type}")


class IPrintProcessor(Protocol):
    def print(self, book: Book) -> None:
        pass


class ConsolePrintProcessor:
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrintProcessor:
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class PrintFactory:
    @staticmethod
    def get(display_type: str) -> IPrintProcessor:
        match display_type:
            case "console":
                return ConsolePrintProcessor()
            case "reverse":
                return ReversePrintProcessor()
            case _:
                raise ValueError(f"Unknown print type: {display_type}")


class ISerializeProcessor(Protocol):
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializeProcessor:
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializeProcessor:
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


class SerializeFactory:
    @staticmethod
    def get(serialize_type: str) -> ISerializeProcessor:
        match serialize_type:
            case "json":
                return JsonSerializeProcessor()
            case "xml":
                return XmlSerializeProcessor()
            case _:
                raise ValueError(f"Unknown serialize type: {serialize_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            proc = DisplayFactory.get(method_type)
            proc.display(book)
        elif cmd == "print":
            proc = PrintFactory.get(method_type)
            proc.print(book)
        elif cmd == "serialize":
            proc = SerializeFactory.get(method_type)
            return proc.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
