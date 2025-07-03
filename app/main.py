import json
import xml.etree.ElementTree as ET  # noqa


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class Display:
    @staticmethod
    def console_display(book: Book) -> None:
        print(book.content)

    @staticmethod
    def reverse_display(book: Book) -> None:
        print(book.content[::-1])

    def display(self, book: Book, method_type: str) -> None:
        if method_type == "console":
            self.console_display(book)
        elif method_type == "reverse":
            self.reverse_display(book)


class Printer:
    @staticmethod
    def console_print(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)

    @staticmethod
    def reverse_print(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])

    def print_book(self, book: Book, method_type: str) -> None:
        if method_type == "console":
            self.console_print(book)
        elif method_type == "reverse":
            self.reverse_print(book)


class Serializer:
    @staticmethod
    def jsonserialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})

    @staticmethod
    def xmlserialize(book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")

    def serialize(self, book: Book, method_type: str) -> None | str:
        if method_type == "json":
            return self.jsonserialize(book)
        elif method_type == "xml":
            return self.xmlserialize(book)
        return None


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            Display().display(book, method_type)
        elif cmd == "print":
            Printer().print_book(book, method_type)
        elif cmd == "serialize":
            return Serializer().serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
