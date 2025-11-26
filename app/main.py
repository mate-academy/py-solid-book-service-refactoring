import json
import xml.etree.ElementTree as ET  # noqa: N817
from abc import ABC, abstractmethod


class BookInterface(ABC):
    @abstractmethod
    def get_title(self) -> None:
        pass

    @abstractmethod
    def get_content(self) -> None:
        pass


class Book(BookInterface):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def get_title(self) -> str:
        return self.title

    def get_content(self) -> str:
        return self.content


class DisplayService(ABC):
    @abstractmethod
    def display(self, book: BookInterface) -> None:
        pass


class DisplayConsole(DisplayService):
    def display(self, book: BookInterface) -> None:
        print(book.get_content())


class DisplayReverse(DisplayService):
    def display(self, book: BookInterface) -> None:
        print(book.get_content()[::-1])


class PrintService(ABC):
    @abstractmethod
    def print(self, book: BookInterface) -> None:
        pass


class PrintConsole(PrintService):
    def print(self, book: BookInterface) -> None:
        print(f"Printing the book: {book.get_title()}...")
        print(book.get_content())


class PrintReverse(PrintService):
    def print(self, book: BookInterface) -> None:
        print(f"Printing the book in reverse: {book.get_title()}...")
        print(book.get_content()[::-1])


class SerializerService(ABC):
    @abstractmethod
    def serialize(self, book: BookInterface) -> None:
        pass


class SerializerJSON(SerializerService):
    def serialize(self, book: BookInterface) -> str:
        return json.dumps(
            {
                "title": book.get_title(), "content": book.get_content()
            }
        )


class SerializerXML(SerializerService):
    def serialize(self, book: BookInterface) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.get_title()
        content = ET.SubElement(root, "content")
        content.text = book.get_content()
        return ET.tostring(root, encoding="unicode")


class BookService:
    def __init__(
            self,
            book: BookInterface,
            displays: list[DisplayService],
            printers: list[PrintService],
            serializers: list[SerializerService],
    ) -> None:
        self.book = book
        self.displays = displays
        self.printers = printers
        self.serializers = serializers

    def execute_command(self, cmd: str, method_type: str = None) -> None | str:
        if cmd == "display":
            for display in self.displays:
                display.display(self.book)
        elif cmd == "print":
            for printer in self.printers:
                printer.print(self.book)
        elif cmd == "serialize":
            if method_type == "json":
                for serializer in self.serializers:
                    if isinstance(serializer, SerializerJSON):
                        return serializer.serialize(self.book)
            if method_type == "xml":
                for serializer in self.serializers:
                    if isinstance(serializer, SerializerXML):
                        return serializer.serialize(self.book)


def main(book: BookInterface, commands: list[str]) -> str:
    displays = [DisplayConsole(), DisplayReverse()]
    printers = [PrintConsole(), PrintReverse()]
    serializers = [SerializerJSON(), SerializerXML()]
    service = BookService(book, displays, printers, serializers)
    result = None
    for cmd, method_type in commands:
        output = service.execute_command(cmd, method_type)
        if cmd == "serialize":
            result = output
    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", None), ("serialize", "json")]))
