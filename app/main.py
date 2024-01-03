import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class ConsoleDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content[::-1])


class PrintStrategy(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        pass


class ConsolePrint(PrintStrategy):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrint(PrintStrategy):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JsonSerialize(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerialize(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        root = ET.Element("book")
        title_element = ET.SubElement(root, "title")
        title_element.text = title
        content_element = ET.SubElement(root, "content")
        content_element.text = content
        return ET.tostring(root, encoding="unicode")


class Book:
    def __init__(
        self,
        title: str,
        content: str,
        display_strategy: DisplayStrategy = ConsoleDisplay(),
        print_strategy: PrintStrategy = ConsolePrint(),
        serialize_strategy: SerializeStrategy = JsonSerialize(),
    ):
        self.title = title
        self.content = content
        self.display_strategy = display_strategy
        self.print_strategy = print_strategy
        self.serialize_strategy = serialize_strategy

    def display(self) -> None:
        self.display_strategy.display(self.content)

    def print_book(self) -> None:
        self.print_strategy.print_book(self.title, self.content)

    def serialize(self) -> str:
        return self.serialize_strategy.serialize(self.title, self.content)


if __name__ == "__main__":
    sample_book = Book(
        "Sample Book",
        "This is some sample content.",
        display_strategy=ReverseDisplay(),
        serialize_strategy=XmlSerialize(),
    )
    sample_book.display()
    print(sample_book.serialize())
