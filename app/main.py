import json
import xml.etree.ElementTree as ETree
from abc import abstractmethod, ABC


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class Display:
    @staticmethod
    def display(book: Book, display_type: str) -> None:
        if display_type == "console":
            print(book.content)
        elif display_type == "reverse":
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {display_type}")


class PrintBook:
    @staticmethod
    def print(book: Book, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {book.title}...")
            print(book.content)
        elif print_type == "reverse":
            print(f"Printing the book in reverse: {book.title}...")
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {print_type}")


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = ETree.Element("book")
        title = ETree.SubElement(root, "title")
        title.text = book.title
        content = ETree.SubElement(root, "content")
        content.text = book.content
        return ETree.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    serializers = {
        "json": JSONSerializer,
        "xml": XMLSerializer
    }
    for cmd, method_type in commands:
        if cmd == "display":
            Display.display(book, method_type)
        elif cmd == "print":
            PrintBook.print(book, method_type)
        elif cmd == "serialize":
            return serializers.get(method_type)().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
