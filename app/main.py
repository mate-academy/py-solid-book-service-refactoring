import json
import xml.etree.ElementTree as ElementTree


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class DisplayStrategy:
    def display(self, book: Book) -> None:
        raise NotImplementedError


class PrintStrategy:
    def print_book(self, book: Book) -> None:
        raise NotImplementedError


class SerializationStrategy:
    def serialize(self, book: Book) -> str:
        raise NotImplementedError


class ConsoleDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class ConsolePrint(PrintStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(PrintStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class JSONSerialization(SerializationStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerialization(SerializationStrategy):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


COMMANDS_MAP = {
    ("display", "console"): ConsoleDisplay(),
    ("display", "reverse"): ReverseDisplay(),
    ("print", "console"): ConsolePrint(),
    ("print", "reverse"): ReversePrint(),
    ("serialize", "json"): JSONSerialization(),
    ("serialize", "xml"): XMLSerialization()
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        strategy = COMMANDS_MAP.get((cmd, method_type))
        if not strategy:
            raise ValueError(
                f"Unknown command or method type: {cmd}, {method_type}"
            )

        if cmd == "display":
            strategy.display(book)
        elif cmd == "print":
            strategy.print_book(book)
        elif cmd == "serialize":
            return strategy.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
