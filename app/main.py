import json
import xml.etree.ElementTree as ET


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def serialize(self, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": self.title, "content": self.content})
        elif serialize_type == "xml":
            root = ET.Element("book")
            title = ET.SubElement(root, "title")
            title.text = self.title
            content = ET.SubElement(root, "content")
            content.text = self.content
            return ET.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")


class Displayer:
    def __init__(self, book):
        self.book = book

    def display_console(self):
        print(self.book.content)

    def display_reverse(self):
        print(self.book.content[::-1])

    def display(self, method_type: str):
        method_name = f"display_{method_type}"
        method = getattr(self, method_name, None)

        if not callable(method):
            raise ValueError(f"Unknown display method: {method_type}")

        method()


class Printer:
    def __init__(self, book):
        self.book = book

    def print_console(self):
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)

    def print_reverse(self):
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])

    def print_content(self, method_type: str):
        method_name = f"print_{method_type}"
        method = getattr(self, method_name, None)

        if not callable(method):
            raise ValueError(f"Unknown print type: {method_type}")

        method()


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display = Displayer(book)
            display.display(method_type)
        elif cmd == "print":
            to_print = Printer(book)
            to_print.print_content(method_type)
        elif cmd == "serialize":
            return book.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("print", "reverse"), ("serialize", "xml")]))
