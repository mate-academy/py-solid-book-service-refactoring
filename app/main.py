import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod


class BookCatalog():
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class Displayable(BookCatalog, ABC):
    @abstractmethod
    def display_console(self, display_type: str) -> None:
        pass

    @abstractmethod
    def display_reverse(self, display_type: str) -> None:
        pass


class DisplayBook(Displayable):
    def display_console(self, display_type: str) -> None:
        if display_type == "console":
            print(self.content)
        else:
            raise ValueError(f"Unknown display type: {display_type}")

    def display_reverse(self, display_type: str) -> None:
        if display_type == "reverse":
            print(self.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {display_type}")


class Printable(BookCatalog, ABC):
    @abstractmethod
    def print_console(self, print_type: str) -> None:
        pass

    @abstractmethod
    def print_reverse(self, print_type: str) -> None:
        pass


class PrintBook(Printable):
    def __init__(self, title: str, content: str) -> None:
        super().__init__(title, content)

    def print_console(self, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {self.title}...")
            print(self.content)
        else:
            raise ValueError(f"Unknown print type: {print_type}")

    def print_reverse(self, print_type: str) -> None:
        if print_type == "reverse":
            print(f"Printing the book in reverse: {self.title}...")
            print(self.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {print_type}")


class Serializable(BookCatalog, ABC):
    @abstractmethod
    def serialize_json(self, serialize_type: str) -> str:
        pass

    @abstractmethod
    def serialize_xml(self, serialize_type: str) -> str:
        pass


class SerializeJsonBook(Serializable):
    def __init__(self, title: str, content: str) -> None:
        super().__init__(title, content)

    def serialize_json(self, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": self.title, "content": self.content})
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")


class SerializeXmlBook(Serializable):
    def __init__(self, title: str, content: str) -> None:
        super().__init__(title, content)

    def serialize_xml(self, serialize_type: str) -> str:
        if serialize_type == "xml":
            root = ElementTree.Element("book")
            title = ElementTree.SubElement(root, "title")
            title.text = self.title
            content = ElementTree.SubElement(root, "content")
            content.text = self.content
            return ElementTree.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")


class Book(DisplayBook, PrintBook, SerializeJsonBook, SerializeXmlBook):
    pass


def main(book: DisplayBook | PrintBook | SerializeJsonBook | SerializeXmlBook,
         commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display" and method_type == "console":
            book.display_console(method_type)
        elif cmd == "display" and method_type == "reverse":
            book.display_reverse(method_type)
        elif cmd == "print" and method_type == "console":
            book.print_console(method_type)
        elif cmd == "print" and method_type == "reverse":
            book.print_reverse(method_type)
        elif cmd == "serialize" and method_type == "json":
            return book.serialize_json(method_type)
        elif cmd == "serialize" and method_type == "xml":
            return book.serialize_xml(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
