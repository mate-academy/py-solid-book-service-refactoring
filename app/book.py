import json
import xml.etree.ElementTree as ElTree


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display_console(self) -> None:
        print(self.content)

    def display_reverse(self) -> None:
        print(self.content[::-1])

    def display_book(self, display_type: str) -> None:
        if display_type == "console":
            self.display_console()
        elif display_type == "reverse":
            self.display_reverse()
        else:
            raise ValueError(f"Unknown display type: {display_type}")

    def print_book_console(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)

    def print_book_reverse(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])

    def print_book(self, print_type: str) -> None:
        if print_type == "console":
            self.print_book_console()
        elif print_type == "reverse":
            self.print_book_reverse()
        else:
            raise ValueError(f"Unknown print type: {print_type}")

    def serialize_json(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})

    def serialize_xml(self) -> str:
        root = ElTree.Element("book")
        title = ElTree.SubElement(root, "title")
        title.text = self.title
        content = ElTree.SubElement(root, "content")
        content.text = self.content
        return ElTree.tostring(root, encoding="unicode")

    def serialize(self, serialize_type: str) -> str:
        if serialize_type == "json":
            return self.serialize_json()
        elif serialize_type == "xml":
            return self.serialize_xml()
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
