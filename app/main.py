import json
from xml.etree import ElementTree
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class DisplayClass(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(DisplayClass):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayClass):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class PrintClass(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrint(PrintClass):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(PrintClass):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content[::-1])


class SerializeClass(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(SerializeClass):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(SerializeClass):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


DISPLAY_COMMANDS = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}

PRINT_COMMANDS = {
    "console": ConsolePrint(),
    "reverse": ReversePrint(),
}

SERIALIZERS = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    result = None

    for cmd, method_type in commands:
        if cmd == "display":
            strategy = DISPLAY_COMMANDS.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown display type: {method_type}")
            strategy.display(book)

        elif cmd == "print":
            strategy = PRINT_COMMANDS.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown print type: {method_type}")
            strategy.print_book(book)

        elif cmd == "serialize":
            serializer = SERIALIZERS.get(method_type)
            if not serializer:
                raise ValueError(f"Unknown serialize type: {method_type}")
            result = serializer.serialize(book)

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
