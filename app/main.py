import json
from xml.etree.ElementTree import Element, SubElement, tostring


class DislayInformationMixin:
    def display(self, display_type: str) -> None:
        if display_type == "console":
            print(self.content)
        elif display_type == "reverse":
            print(self.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {display_type}")


class PrintMixin:

    def print_title(self, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {self.title}...")
        else:
            print(f"Printing the book in {print_type}: {self.title}...")

    def print_book(self, print_type: str) -> None:
        self.print_title(print_type)
        if print_type == "console":
            print(self.content)
        elif print_type == "reverse":
            print(self.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {print_type}")


class SerializingMixin:
    def serialize(self, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": self.title, "content": self.content})
        elif serialize_type == "xml":
            root = Element("book")
            title = SubElement(root, "title")
            title.text = self.title
            content = SubElement(root, "content")
            content.text = self.content
            return tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")


class Book(DislayInformationMixin, PrintMixin, SerializingMixin):
    def __init__(self, title: str, content: str) -> None:
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
