import json
import xml.etree.ElementTree as Et
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class Display(ABC):
    def __init__(self, book: Book, display_type: str) -> None:
        self.display_type = display_type
        self.book = book

    @abstractmethod
    def display(self) -> None:
        pass


class DisplayConsole(Display):
    def display(self) -> None:
        print(self.book.content)


class DisplayReverse(Display):
    def display(self) -> None:
        print(self.book.content[::-1])


class DisplayError(Display):
    def display(self) -> None:
        raise ValueError(f"Unknown display type: {self.display_type}")


class PrintBook(ABC):
    def __init__(self, book: Book, print_type: str) -> None:
        self.print_type = print_type
        self.book = book

    @abstractmethod
    def display(self) -> None:
        pass


class PrintBookConsole(PrintBook):
    def display(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class PrintBookReverse(PrintBook):
    def display(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])


class PrintBookError(PrintBook):
    def display(self) -> None:
        raise ValueError(f"Unknown print type: {self.print_type}")


class Serialize(ABC):
    def __init__(self, book: Book, serialize_type: str) -> None:
        self.serialize_type = serialize_type
        self.book = book

    @abstractmethod
    def display(self) -> str:
        pass


class SerializeJson(Serialize):
    def display(self) -> str:
        return json.dumps(
            {"title": self.book.title, "content": self.book.content}
        )


class SerializeXml(Serialize):
    def display(self) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = self.book.title
        content = Et.SubElement(root, "content")
        content.text = self.book.content
        return Et.tostring(root, encoding="unicode")


class SerializeError(Serialize):
    def display(self) -> str:
        raise ValueError(f"Unknown serialize type: {self.serialize_type}")


ACTION_TYPES = {
    "display": {
        "console": DisplayConsole,
        "reverse": DisplayReverse,
        None: DisplayError
    },
    "print": {
        "console": PrintBookConsole,
        "reverse": PrintBookReverse,
        None: PrintBookError
    },
    "serialize": {
        "json": SerializeJson,
        "xml": SerializeXml,
        None: SerializeError
    }
}


def perform_action(
    action_type: str,
    book: Book,
    method_type: str
) -> None | str:
    if method_type not in ["console", "reverse", "json", "xml"]:
        action = ACTION_TYPES[action_type][None](book, method_type)
        return action.display()

    action = ACTION_TYPES[action_type][method_type](book, method_type)
    return action.display()


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for action_type, method_type in commands:
        if action_type in ACTION_TYPES:
            return perform_action(action_type, book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
