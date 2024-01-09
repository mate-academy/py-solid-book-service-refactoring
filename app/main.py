import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod


class ReverseAuth:
    @staticmethod
    def is_console(method_type: str) -> bool:
        if method_type == "reverse":
            return True


class ConsoleAuth:
    @staticmethod
    def is_console(method_type: str) -> bool:
        if method_type == "console":
            return True


class JsonAuth:
    @staticmethod
    def is_json(serialize_type: str) -> bool:
        if serialize_type == "json":
            return True


class XmlAuth:
    @staticmethod
    def is_console(serialize_type: str) -> bool:
        if serialize_type == "xml":
            return True


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class BookDisplay(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class DisplayConsoleProcessor(BookDisplay):
    def __init__(self, display_type: str, authorizer: ConsoleAuth) -> None:
        self.display_type = display_type
        self.authorizer = authorizer

    def display(self, book: Book) -> None:
        if self.authorizer:
            print(book.content)


class DisplayReverseProcessor(BookDisplay):
    def __init__(self, display_type: str, authorizer: ReverseAuth) -> None:
        self.display_type = display_type
        self.authorizer = authorizer

    def display(self, book: Book) -> None:
        if self.authorizer:
            print(book.content[::-1])


class BookPrinter(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class PrinterConsoleProcessor(BookPrinter):
    def __init__(self, print_type: str, authorizer: ConsoleAuth) -> None:
        self.print_type = print_type
        self.authorizer = authorizer

    def print_book(self, book: Book) -> None:
        if self.authorizer:
            print(f"Printing the book: {book.title}...")
            print(book.content)


class PrinterReverseProcessor(BookPrinter):
    def __init__(self, print_type: str, authorizer: ReverseAuth) -> None:
        self.print_type = print_type
        self.authorizer = authorizer

    def print_book(self, book: Book) -> None:
        if self.authorizer:
            print(f"Printing the book in reverse: {book.title}...")
            print(book.content[::-1])


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class SerializerJson(BookSerializer):
    def __init__(self, serialize_type: str, authorizer: JsonAuth) -> None:
        self.serialize_type = serialize_type
        self.authorizer = authorizer

    def serialize(self, book: Book) -> str:
        if self.authorizer:
            return json.dumps({"title": book.title, "content": book.content})


class SerializerXML(BookSerializer):
    def __init__(self, serialize_type: str, authorizer: XmlAuth) -> None:
        self.serialize_type = serialize_type
        self.authorizer = authorizer

    def serialize(self, book: Book) -> str:
        if self.authorizer:
            root = ElementTree.Element("book")
            title = ElementTree.SubElement(root, "title")
            title.text = book.title
            content = ElementTree.SubElement(root, "content")
            content.text = book.content
            return ElementTree.tostring(root, encoding="unicode")


# class SerializerHandler(SerializerJson, SerializerXML)
def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    console_auth = ConsoleAuth()
    reverse_auth = ReverseAuth()
    json_auth = JsonAuth()
    xml_auth = XmlAuth()
    display_processors = {
        "console": DisplayConsoleProcessor("console", console_auth),
        "reverse": DisplayReverseProcessor("reverse", reverse_auth),
    }

    printer_processors = {
        "console": PrinterConsoleProcessor("console", console_auth),
        "reverse": PrinterReverseProcessor("reverse", reverse_auth),
    }

    serializer_processors = {
        "json": SerializerJson("json", json_auth),
        "xml": SerializerXML("xml", xml_auth),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            display_processor = display_processors.get(method_type)
            if display_processor:
                display_processor.display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            printer_processor = printer_processors.get(method_type)
            if printer_processor:
                printer_processor.print_book(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            serializer_processor = serializer_processors.get(method_type)
            if serializer_processor:
                return serializer_processor.serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "json")]))
