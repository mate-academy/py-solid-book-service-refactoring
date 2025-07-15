import json
import xml.etree.ElementTree as ET


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


class DisplayBook:
    def display_console(self, book: Book):
        print(book.content)

    def display_reverse(self, book: Book):
        print(book.content[::-1])


class PrintBook:
    def print_console(self, book: Book):
        print(f"Printing the book: {book.title}...")
        print(book.content)

    def print_reverse(self, book: Book):
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class SerializeBook:
    def serialize_json(self, book: Book):
        return json.dumps({"title": book.title, "content": book.content})

    def serialize_xml(self, book: Book):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            displayer = DisplayBook()
            if method_type == "console":
                displayer.display_console(book)
            elif method_type == "reverse":
                displayer.display_reverse(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            printer = PrintBook()
            if method_type == "console":
                printer.print_console(book)
            elif method_type == "reverse":
                printer.print_reverse(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            serializer = SerializeBook()
            if method_type == "json":
                return serializer.serialize_json(book)
            elif method_type == "xml":
                return serializer.serialize_xml(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))