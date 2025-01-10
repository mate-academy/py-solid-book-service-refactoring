import json
import xml.etree.ElementTree as ETree
from dataclasses import dataclass
from abc import abstractmethod, ABC


@dataclass
class Book:

    title: str
    content: str


class Display(ABC):

    @staticmethod
    @abstractmethod
    def run(book: Book) -> None:
        pass


class ConsoleDisplay(Display):

    @staticmethod
    def run(book: Book) -> None:
        print(book.content)


class ReverseDisplay(Display):

    @staticmethod
    def run(book: Book) -> None:
        print(book.content[::-1])


class Print(ABC):

    @staticmethod
    @abstractmethod
    def run(book: Book) -> None:
        pass


class ConsolePrint(Print):

    @staticmethod
    def run(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(Print):

    @staticmethod
    def run(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class Serialize(ABC):

    @staticmethod
    @abstractmethod
    def run(book: Book) -> str:
        pass


class JsonSerialize(Serialize):

    @staticmethod
    def run(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerialize(Serialize):

    @staticmethod
    def run(book: Book) -> str:
        root = ETree.Element("book")
        title = ETree.SubElement(root, "title")
        title.text = book.title
        content = ETree.SubElement(root, "content")
        content.text = book.content
        return ETree.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:

    service = {
        "display": {
            "console": ConsoleDisplay(),
            "reverse": ReverseDisplay()
        },
        "print": {
            "console": ConsolePrint(),
            "reverse": ReversePrint(),
        },
        "serialize": {
            "json": JsonSerialize(),
            "xml": XMLSerialize()
        }
    }

    for cmd, method_type in commands:

        method = service[cmd][method_type]
        if not method:
            raise ValueError(f"Unknown {cmd} type: {method_type}")

        if isinstance(method, Serialize):
            return method.run(book)

        method.run(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
