
import json
import xml.etree.ElementTree as ElementTree


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class BookDisplay:
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self, display_type: str) -> None:
        if display_type == "console":
            print(self.book.content)
        elif display_type == "reverse":
            print(self.book.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {display_type}")


class BookPrint:
    def __init__(self, book: Book) -> None:
        self.book = book

    def print_book(self, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {self.book.title}...")
            print(self.book.content)
        elif print_type == "reverse":
            print(f"Printing the book in reverse: {self.book.title}...")
            print(self.book.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {print_type}")


class BookSerializer:
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps(
                {"title": self.book.title, "content": self.book.content}
            )
        elif serialize_type == "xml":
            root = ElementTree.Element("book")
            title = ElementTree.SubElement(root, "title")
            title.text = self.book.title
            content = ElementTree.SubElement(root, "content")
            content.text = self.book.content
            return ElementTree.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
