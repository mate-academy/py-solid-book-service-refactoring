import json
import xml.etree.ElementTree as ET # noqa


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class DisplayBook:
    def __init__(self, display_type: str) -> None:
        self._display_type = display_type

    @staticmethod
    def _console_display(book: Book) -> None:
        print(book.content)

    @staticmethod
    def _reverse_display(book: Book) -> None:
        print(book.content[::-1])

    def display(self, book: Book) -> None:
        if self._display_type == "console":
            self._console_display(book)
        elif self._display_type == "reverse":
            self._reverse_display(book)
        else:
            raise ValueError(f"Unknown display type: {self._display_type}")


class PrintBook:
    def __init__(self, print_type: str) -> None:
        self._print_type = print_type

    @staticmethod
    def _console_print(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)

    @staticmethod
    def _reverse_print(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])

    def print_book(self, book: Book) -> None:
        if self._print_type == "console":
            self._console_print(book)
        elif self._print_type == "reverse":
            self._reverse_print(book)
        else:
            raise ValueError(f"Unknown print type: {self._print_type}")


class BookSerializer:
    def __init__(self, serialize_type: str) -> None:
        self._serialize_type = serialize_type

    @staticmethod
    def _json_serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})

    @staticmethod
    def _xml_serialize(book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")

    def serialize(self, book: Book) -> str:
        if self._serialize_type == "json":
            return self._json_serialize(book)
        elif self._serialize_type == "xml":
            return self._xml_serialize(book)
        else:
            raise ValueError(f"Unknown serialize type: {self._serialize_type}")


def display_book(book: Book, display_type: str) -> None:
    display = DisplayBook(display_type)
    display.display(book)


def print_book(book: Book, print_type: str) -> None:
    my_print = PrintBook(print_type)
    my_print.print_book(book)


def serialize_book(book: Book, serializer_type: str) -> str:
    serializer = BookSerializer(serializer_type)
    return serializer.serialize(book)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_book(book, method_type)
        elif cmd == "print":
            print_book(book, method_type)
        elif cmd == "serialize":
            return serialize_book(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
