import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def display(self, content) -> None:
        pass


class DisplayConsole(Display):
    def display(self, content) -> None:
        print(content)


class DisplayReverse(Display):
    def display(self, content) -> None:
        print(content[::-1])


class DisplayManager:
    display_managers = {}

    def __init__(self, content: str):
        self.content = content

        self.display_managers["console"] = DisplayConsole()
        self.display_managers["reverse"] = DisplayReverse()

    def display(self, method_type) -> None:
        display_manager = self.display_managers.get(method_type)
        if display_manager:
            display_manager.display(self.content)
        else:
            print(f"Invalid method_type: {method_type}")


class Print(ABC):
    @abstractmethod
    def print_book(self, title, content) -> None:
        pass


class PrintConsole(Print, DisplayConsole):
    def print_book(self, title, content) -> None:
        print(f"Printing the book: {title}...")
        self.display(content)


class PrintReverse(Print, DisplayReverse):
    def print_book(self, title, content) -> None:
        print(f"Printing the book in reverse: {title}...")
        self.display(content)


class PrintManager:
    print_managers = {}

    def __init__(self, title, content):
        self.title = title
        self.content = content

        self.print_managers["console"] = PrintConsole()
        self.print_managers["reverse"] = PrintReverse()

    def print_book(self, method_type) -> None:
        print_manager = self.print_managers.get(method_type)
        if print_manager:
            print_manager.print_book(self.title, self.content)
        else:
            print(f"Invalid method_type: {method_type}")


class Serialize(ABC):
    @abstractmethod
    def serialize(self, book) -> str:
        pass


class SerializeJson(Serialize):
    def serialize(self, book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeXml(Serialize):
    def serialize(self, book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


class SerializeManager:
    serialize_managers = {}

    def __init__(self, book):
        self.book = book

        self.serialize_managers["json"] = SerializeJson()
        self.serialize_managers["xml"] = SerializeXml()

    def serialize(self, method_type) -> str:
        serialize_manager = self.serialize_managers.get(method_type)
        if serialize_manager:
            return serialize_manager.serialize(self.book)
        else:
            print(f"Invalid method_type: {method_type}")


class Book(DisplayManager, PrintManager, SerializeManager):
    def __init__(self, title: str, content: str):
        DisplayManager.__init__(self, content)
        PrintManager.__init__(self, title, content)
        SerializeManager.__init__(self, self)
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        elif cmd == "print":
            book.print_book(method_type)
        elif cmd == "serialize":
            return book.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))