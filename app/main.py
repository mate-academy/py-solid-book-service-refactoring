import json
import xml.etree.ElementTree as Et
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class Display(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class DisplayOut(Display):
    def display(self, content: str) -> None:
        print(content)


class DisplayReverse(Display):
    def display(self, content: str) -> None:
        print(content[::-1])


class OutputBookHandler(ABC):
    @abstractmethod
    def output(self, book: Book, output_type: Display) -> None:
        pass


class DisplayOutput(OutputBookHandler):
    def output(self, book: Book, output_type: Display) -> None:
        print(f"Displaying the book: {book.title}...")
        output_type.display(book.content)


class PrintOutput(OutputBookHandler):
    def output(self, book: Book, output_type: Display) -> None:
        print(f"Printing the book: {book.title}...")
        output_type.display(book.content)


class Serialize(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializeOutput(Serialize):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializeOutput(Serialize):
    def serialize(self, book: Book) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = book.title
        content = Et.SubElement(root, "content")
        content.text = book.content
        return Et.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display" or cmd == "print":
            if method_type == "reverse":
                output_content_type = DisplayReverse()
            elif method_type == "console":
                output_content_type = DisplayOut()
            else:
                raise ValueError(f"Unknown output type: {method_type}")

            if cmd == "display":
                output_book_handler = DisplayOutput()
            elif cmd == "print":
                output_book_handler = PrintOutput()

            output_book_handler.output(book, output_content_type)
        elif cmd == "serialize":
            if method_type == "json":
                serializer = JsonSerializeOutput()
            elif method_type == "xml":
                serializer = XmlSerializeOutput()
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serializer.serialize(book)
        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
