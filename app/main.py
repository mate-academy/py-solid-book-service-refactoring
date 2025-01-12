import json
import xml.etree.ElementTree as ET


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


class DisplayBook:
    def display_console(book: Book) -> None:
        print(book.content)

    def display_reverse(book: Book) -> None:
        print(book.content[::-1])


class PrintBook:
    def print_console(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)

    def print_reverse(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class SerializeBook:
    def serialize_json(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})

    def serialize_xml(book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                DisplayBook.display_console(book)
            elif method_type == "reverse":
                DisplayBook.display_reverse(book)
        elif cmd == "print":
            if method_type == "console":
                PrintBook.print_console(book)
            elif method_type == "reverse":
                PrintBook.print_reverse(book)
        elif cmd == "serialize":
            if method_type == "json":
                return SerializeBook.serialize_json(book)
            elif method_type == "xml":
                return SerializeBook.serialize_xml(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
