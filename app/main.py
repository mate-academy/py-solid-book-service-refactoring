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
    def print_book(self, title) -> None:
        pass


class PrintConsole(Print):
    def print_book(self, title) -> None:
        print(f"Printing the book: {title}...")


class PrintReverse(Print):
    def print_book(self, title) -> None:
        print(f"Printing the book in reverse: {title}...")


class PrintManager:
    print_managers = {}

    def __init__(self, title):
        self.title = title

        self.print_managers["console"] = PrintConsole()
        self.print_managers["reverse"] = PrintReverse()

    def print_book(self, method_type) -> None:
        print_manager = self.print_managers.get(method_type)
        if print_manager:
            print_manager.print_book(self.title)
        else:
            print(f"Invalid method_type: {method_type}")


class Serialize(ABC):
    @abstractmethod
    def serialize(self, title, content) -> str:
        pass


class SerializeJson(Serialize):
    def serialize(self, title, content) -> str:
        return json.dumps({"title": title, "content": content})


class SerializeXml(Serialize):
    def serialize(self, title, content) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = title
        content = ET.SubElement(root, "content")
        content.text = content
        return ET.tostring(root, encoding="unicode")


class SerializeManager:
    serialize_managers = {}

    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

        self.serialize_managers["json"] = SerializeJson()
        self.serialize_managers["xml"] = SerializeXml()

    def serialize(self, method_type) -> str:
        serialize_manager = self.serialize_managers.get(method_type)
        if serialize_manager:
            return serialize_manager.serialize(self.title, self.content)
        else:
            return f"Invalid method_type: {method_type}"


class Book(DisplayManager, PrintManager, SerializeManager):
    def __init__(self, title: str, content: str):
        DisplayManager.__init__(self, content)
        PrintManager.__init__(self, title)
        SerializeManager.__init__(self, title, content)
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
