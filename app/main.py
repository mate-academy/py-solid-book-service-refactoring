import json
from xml.etree import ElementTree


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class DisplayBook:
    @staticmethod
    def console(book: Book) -> None:
        print(book.content)

    @staticmethod
    def reverse(book: Book) -> None:
        print(book.content[::-1])


class PrintBook:
    @staticmethod
    def console(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)

    @staticmethod
    def reverse(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class SerializableBook:
    @staticmethod
    def json(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})

    @staticmethod
    def xml(book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            getattr(DisplayBook, method_type)(book)
        elif cmd == "print":
            getattr(PrintBook, method_type)(book)
        elif cmd == "serialize":
            return getattr(SerializableBook, method_type)(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
