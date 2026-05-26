import json
import xml.etree.ElementTree as xml_ET
from enum import Enum, auto
from dataclasses import dataclass, asdict
from abc import ABC, abstractmethod


@dataclass
class Book:
    title: str
    content: str


# Abstract classes
class BaseDisplay(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class BasePrint(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class BaseSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


# ----------------|


# Display classes
class ConsoleDisplay(BaseDisplay):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(BaseDisplay):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class Viewer:
    def __init__(self, displayer: BaseDisplay) -> None:
        self._displayer = displayer

    def display(self, book: Book) -> None:
        self._displayer.display(book)


# ---------------|


# Print classes
class ConsolePrint(BasePrint):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(BasePrint):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class Printer:
    def __init__(self, printer: BasePrint) -> None:
        self._printer = printer

    def print(self, book: Book) -> None:
        self._printer.print(book)


# -------------|


# Check classes
class JsonSerializer(BaseSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps(asdict(book))


class XmlSerializer(BaseSerializer):
    def serialize(self, book: Book) -> str:
        root = xml_ET.Element("book")
        for element, text in asdict(book).items():
            sub_element = xml_ET.SubElement(root, element)
            sub_element.text = text
        return xml_ET.tostring(root, encoding="unicode")


class Serializer:
    def __init__(self, serializer: BaseSerializer) -> None:
        self._serializer = serializer

    def serialize(self, book: Book) -> str:
        return self._serializer.serialize(book)


# -------------|


class ConsoleCommands(str, Enum):
    display = auto()
    print = auto()
    serialize = auto()


class BaseConsoleCommandsType(str, Enum):
    console = auto()
    reverse = auto()


class SerializeCommands(str, Enum):
    json = auto()
    xml = auto()


DISPLAY_MAP: dict[str, BaseDisplay] = {
    BaseConsoleCommandsType.console.name: ConsoleDisplay(),
    BaseConsoleCommandsType.reverse.name: ReverseDisplay(),
}

PRINT_MAP: dict[str, BasePrint] = {
    BaseConsoleCommandsType.console.name: ConsolePrint(),
    BaseConsoleCommandsType.reverse.name: ReversePrint(),
}

SERIALIZE_MAP: dict[str, BaseSerializer] = {
    SerializeCommands.json.name: JsonSerializer(),
    SerializeCommands.xml.name: XmlSerializer(),
}

COMMAND_MAP = {
    ConsoleCommands.display.name: (DISPLAY_MAP, Viewer),
    ConsoleCommands.print.name: (PRINT_MAP, Printer),
    ConsoleCommands.serialize.name: (SERIALIZE_MAP, Serializer),
}


def main(book: Book, commands: list[tuple[str, str]]) -> None:
    for cmd, method_type in commands:
        handler_map, handler_class = COMMAND_MAP[cmd]
        handler = handler_class(handler_map[method_type])
        handler_class_method = getattr(handler, cmd)
        if handler_class_method:
            return handler_class_method(book)


if __name__ == "__main__":
    sample_book = Book(
        title="Sample Book",
        content="This is some sample content."
    )
    print(
        main(
            sample_book, [("display", "reverse"), ("serialize", "xml")]
        )
    )
