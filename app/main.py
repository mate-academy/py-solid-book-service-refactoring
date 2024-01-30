import json
import xml.etree.ElementTree


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class BookDisplay:
    def __init__(self) -> None:
        self.display_strategies = {
            "console": self.display_console,
            "reverse": self.display_reverse,
        }

    def display(self, book: Book, display_type: str) -> None:
        display_strategy = self.display_strategies.get(display_type)
        if display_strategy:
            display_strategy(book)
        else:
            raise ValueError(f"Unknown display type: {display_type}")

    def display_console(self, book: Book) -> None:
        print(book.content)

    def display_reverse(self, book: Book) -> None:
        print(book.content[::-1])


class BookPrinter:
    def print_book(self, book: Book, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {book.title}...")
            print(book.content)
        elif print_type == "reverse":
            print(f"Printing the book in reverse: {book.title}...")
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {print_type}")


class BookSerializer:
    def serialize(self, book: Book, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": book.title, "content": book.content})
        elif serialize_type == "xml":
            root = xml.etree.ElementTree.Element("book")
            title = xml.etree.ElementTree.SubElement(root, "title")
            title.text = book.title
            content = xml.etree.ElementTree.SubElement(root, "content")
            content.text = book.content
            return xml.etree.ElementTree.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display = BookDisplay()
    printer = BookPrinter()
    serializer = BookSerializer()

    for cmd, method_type in commands:
        if cmd == "display":
            display.display(book, method_type)
        elif cmd == "print":
            printer.print_book(book, method_type)
        elif cmd == "serialize":
            return serializer.serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
