import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class Display(ABC):
    @abstractmethod
    def display_type(self, obj: Book) -> None:
        pass


class DisplayConsole(Display):
    def display_type(self, obj: Book) -> None:
        print(obj.content)


class DisplayReverse(Display):
    def display_type(self, obj: Book) -> None:
        print(obj.content[::-1])


class Print(ABC):
    @abstractmethod
    def print_type(self, obj: Book) -> None:
        pass


class PrintConsole(Print):
    def print_type(self, obj: Book) -> None:
        print(f"Printing the book: {obj.title}...")
        print(obj.content)


class PrintReverse(Print):
    def print_type(self, obj: Book) -> None:
        print(f"Printing the book in reverse: {obj.title}...")
        print(obj.content[::-1])


class Serialize(ABC):
    @abstractmethod
    def serializer_type(self, obj: Book) -> None:
        pass


class SerializeJson(ABC):
    def serializer_type(self, obj: Book) -> callable:
        return json.dumps({"title": obj.title, "content": obj.content})


class SerializeXml(ABC):
    def serializer_type(self, obj: Book) -> callable:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = obj.title
        content = ElementTree.SubElement(root, "content")
        content.text = obj.content
        return ElementTree.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        name_class = cmd.capitalize() + method_type.capitalize()
        if cmd == "display":
            globals()[name_class]().display_type(book)
        elif cmd == "print":
            globals()[name_class]().print_type(book)
        elif cmd == "serialize":
            return globals()[name_class]().serializer_type(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
