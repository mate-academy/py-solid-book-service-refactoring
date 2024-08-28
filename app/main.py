import json
import xml
import xml.etree.ElementTree as ET


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class DisplayBook(Book):
    def __init__(self, book: Book) -> None:
        super().__init__(title=book.title, content=book.content)

    def display_console(self) -> None:
        print(self.content)

    def display_reverse(self) -> None:
        print(self.content[::-1])


class PrintBook(Book):
    def __init__(self, book: Book) -> None:
        super().__init__(title=book.title, content=book.content)

    def print_console(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)

    def print_reverse(self) -> None:
        print(f"Printing the book in reverse: {self.title}")
        print(self.content[::-1])


class SerializeBook(Book):
    def __init__(self, book: Book) -> None:
        super().__init__(title=book.title, content=book.content)

    def serialize_json(self) -> json:
        return json.dumps({
            "title": self.title,
            "content": self.content
        })

    def serialize_xml(self) -> xml:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.title
        content = ET.SubElement(root, "content")
        content.text = self.content
        return ET.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_book = DisplayBook(book)
    print_book = PrintBook(book)
    serializer_book = SerializeBook(book)
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                display_book.display_console()
            else:
                display_book.display_reverse()
        elif cmd == "print":
            if method_type == "console":
                print_book.print_console()
            else:
                print_book.print_reverse()
        else:
            if method_type == "json":
                return serializer_book.serialize_json()
            else:
                return serializer_book.serialize_xml()
