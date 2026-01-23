import json
import xml.etree.ElementTree
from abc import ABC, abstractmethod


# class Book:
#     def __init__(self, title: str, content: str):
#         self.title = title
#         self.content = content
#
#     def display(self, display_type: str) -> None:
#         if display_type == "console":
#             print(self.content)
#         elif display_type == "reverse":
#             print(self.content[::-1])
#         else:
#             raise ValueError(f"Unknown display type: {display_type}")
#
#     def print_book(self, print_type: str) -> None:
#         if print_type == "console":
#             print(f"Printing the book: {self.title}...")
#             print(self.content)
#         elif print_type == "reverse":
#             print(f"Printing the book in reverse: {self.title}...")
#             print(self.content[::-1])
#         else:
#             raise ValueError(f"Unknown print type: {print_type}")
#
#     def serialize(self, serialize_type: str) -> str:
#         if serialize_type == "json":
#             return json.dumps({"title": self.title, "content": self.content})
#         elif serialize_type == "xml":
#             root = ET.Element("book")
#             title = ET.SubElement(root, "title")
#             title.text = self.title
#             content = ET.SubElement(root, "content")
#             content.text = self.content
#             return ET.tostring(root, encoding="unicode")
#         else:
#             raise ValueError(f"Unknown serialize type: {serialize_type}")

class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


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


class AbstractPrinter(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrinter(AbstractPrinter):

    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(f"Content: {book.content}")


class ReversePrinter(AbstractPrinter):

    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(f"Content: {book.content[::-1]}")


class AbstractSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONSerializer(AbstractSerializer):

    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(AbstractSerializer):

    def serialize(self, book: Book) -> str:
        root = xml.etree.ElementTree.Element("book")
        title = xml.etree.ElementTree.SubElement(root, "title")
        title.text = book.title
        content = xml.etree.ElementTree.SubElement(root, "content")
        content.text = book.content
        return xml.etree.ElementTree.tostring(root, encoding="unicode")


class Action(ABC):
    @abstractmethod
    def execute(self, book: Book, mode: str) -> None | str:
        pass


class DisplayAction(Action):
    def __init__(self, displayers: dict[str, Display]) -> None:
        self.displayers = displayers

    def execute(self, book: Book, mode: str) -> None:
        self.displayers[mode].display(book)


class PrintAction(Action):
    def __init__(self, printers: dict[str, AbstractPrinter]) -> None:
        self.printers = printers

    def execute(self, book: Book, mode: str) -> None:
        self.printers[mode].print_book(book)


class SerializerAction(Action):
    def __init__(self, serializers: dict[str, AbstractSerializer]) -> None:
        self.serializers = serializers

    def execute(self, book: Book, mode: str) -> str:
        return self.serializers[mode].serialize(book)


ACTIONS = {
    "display": DisplayAction(
        displayers={
            "console": ConsoleDisplay(),
            "reverse": ReverseDisplay()
        }
    ),
    "print": PrintAction(
        printers={
            "console": ConsolePrinter(),
            "reverse": ReversePrinter()
        }
    ),
    "serialize": SerializerAction(
        serializers={
            "json": JSONSerializer(),
            "xml": XMLSerializer()
        }
    ),
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    result = None
    for action_name, mode in commands:
        result = ACTIONS[action_name].execute(book, mode)

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
