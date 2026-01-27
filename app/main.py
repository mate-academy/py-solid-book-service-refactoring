import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: Book): pass


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str: pass


class Command(ABC):
    @abstractmethod
    def execute(self, book: Book, method_type: str) -> str | None:
        pass


class ConsoleDisplay(DisplayStrategy):
    def display(self, book: Book):
        print(book.content)


class ReverseDisplay(DisplayStrategy):
    def display(self, book: Book):
        print(book.content[::-1])


class ConsolePrint(DisplayStrategy):
    def display(self, book: Book):
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(DisplayStrategy):
    def display(self, book: Book):
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class SerializeJson(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeXml(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


class DisplayCommand(Command):
    def __init__(self):
        self._strategies = {
            "console": ConsoleDisplay(),
            "reverse": ReverseDisplay(),
        }

    def execute(self, book: Book, method_type: str) -> None:
        strategy = self._strategies.get(method_type)
        if not strategy:
            raise ValueError(f"Unknow display type: {method_type}")
        strategy.display(book)


class PrintCommand(Command):
    def __init__(self):
        self._strategies = {
            "console": ConsolePrint(),
            "reverse": ReversePrint(),
        }

    def execute(self, book: Book, method_type: str) -> None:
        strategy = self._strategies.get(method_type)
        if not strategy:
            raise ValueError(f"Unknow print type: {method_type}")
        strategy.display(book)


class SerializeCommand(Command):
    def __init__(self):
        self._strategies = {
            "json": SerializeJson(),
            "xml": SerializeXml(),
        }

    def execute(self, book: Book, method_type: str) -> str:
        strategy = self._strategies.get(method_type)
        if not strategy:
            raise ValueError(f"Unknow serialization type: {method_type}")
        return strategy.serialize(book)


COMMANDS = {
    "display": DisplayCommand(),
    "print": PrintCommand(),
    "serialize": SerializeCommand(),
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        command_handler = COMMANDS.get(cmd)

        if not command_handler:
            raise ValueError(f"Unknown command: {cmd}")

        result = command_handler.execute(book, method_type)

        if result:
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
