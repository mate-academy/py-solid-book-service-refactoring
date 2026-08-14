import json
import xml.etree.ElementTree as ET


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class BookConsoleDisplayer:
    @staticmethod
    def display(book: Book, display_type: str) -> None:
        if display_type == "console":
            print(book.content)
        elif display_type == "reverse":
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {display_type}")


class BookPrinter:
    @staticmethod
    def print_book(book: Book, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {book.title}...")
            print(book.content)
        elif print_type == "reverse":
            print(f"Printing the book in reverse: {book.title}...")
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {print_type}")


class JsonSerializer:
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer:
    @staticmethod
    def serialize(book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displayer = BookConsoleDisplayer()
    printer = BookPrinter()

    for cmd, method_type in commands:
        if cmd == "display":
            displayer.display(book, method_type)
        elif cmd == "print":
            printer.print_book(book, method_type)
        elif cmd == "serialize":
            if method_type == "json":
                return JsonSerializer.serialize(book)
            elif method_type == "xml":
                return XmlSerializer.serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
