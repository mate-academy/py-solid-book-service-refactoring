import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod


class BaseBook(ABC):
    DISPLAY_TYPES = ("console", "reverse")
    SERIALIZE_TYPES = ("json", "xml")

    def check_display_type(self, command: str, type_to_check: str) -> None:
        if type_to_check not in self.DISPLAY_TYPES:
            raise ValueError(f"Unknown {command} type: {type_to_check}")

    def check_serializer_type(self, command: str, type_to_check: str) -> None:
        if type_to_check not in self.SERIALIZE_TYPES:
            raise ValueError(f"Unknown {command} type: {type_to_check}")

    @abstractmethod
    def display(self, display_type: str) -> None:
        ...

    @abstractmethod
    def display_console(self) -> None:
        ...

    @abstractmethod
    def display_reverse(self) -> None:
        ...

    @abstractmethod
    def print(self, print_type: str) -> None:
        ...

    @abstractmethod
    def print_console(self) -> None:
        ...

    @abstractmethod
    def print_reverse(self) -> None:
        ...

    @abstractmethod
    def serialize(self, serialize_type: str) -> str:
        ...

    @abstractmethod
    def serialize_json(self) -> str:
        ...

    @abstractmethod
    def serialize_xml(self) -> str:
        ...


class Book(BaseBook):

    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, display_type: str) -> None:
        self.check_display_type("display", display_type)

        getattr(self, f"display_{display_type}")()

    def display_console(self) -> None:
        print(self.content)

    def display_reverse(self) -> None:
        print(self.content[::-1])

    def print(self, print_type: str) -> None:
        self.check_display_type("print", print_type)

        getattr(self, f"print_{print_type}")()

    def print_console(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)

    def print_reverse(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])

    def serialize(self, serialize_type: str) -> str:
        self.check_serializer_type("serialize", serialize_type)
        return getattr(self, f"serialize_{serialize_type}")()

    def serialize_json(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})

    def serialize_xml(self) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.content
        return ElementTree.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd in ("display", "print"):
            getattr(book, f"{cmd}_{method_type}")()

        return getattr(book, f"{cmd}_{method_type}")()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(
        main(sample_book,
             [
                 ("display", "reverse"),
                 ("serialize", "xml")
             ]
             )
    )
