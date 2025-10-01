import json
import xml.etree.ElementTree as ET  # noqa: N817,N813
from abc import ABC, abstractmethod
from typing import Optional, List, Tuple


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


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


class Serializer(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        root = ET.Element("book")
        title_elem = ET.SubElement(root, "title")
        title_elem.text = title
        content_elem = ET.SubElement(root, "content")
        content_elem.text = content
        return ET.tostring(root, encoding="unicode")


class BookManager:
    def __init__(self, book: Book) -> None:
        self.book = book

    def execute(self, strategy: object) -> Optional[str]:
        if isinstance(strategy, DisplayStrategy):
            strategy.display(self.book.content)
        elif isinstance(strategy, PrintStrategy):
            strategy.print_book(self.book.title, self.book.content)
        elif isinstance(strategy, Serializer):
            return strategy.serialize(self.book.title, self.book.content)
        else:
            raise ValueError(f"Unknown strategy type: {type(strategy)}")


def main(book: Book, actions: List[Tuple[str, str]]) -> Optional[str]:
    manager = BookManager(book)
    result: Optional[str] = None

    for action_type, action_value in actions:
        if action_type == "display":
            if action_value == "console":
                manager.execute(ConsoleDisplay())
            elif action_value == "reverse":
                manager.execute(ReverseDisplay())
        elif action_type == "print":
            if action_value == "console":
                manager.execute(ConsolePrint())
            elif action_value == "reverse":
                manager.execute(ReversePrint())
        elif action_type == "serialize":
            if action_value == "json":
                result = manager.execute(JsonSerializer())
            elif action_value == "xml":
                result = manager.execute(XmlSerializer())
    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    main(sample_book, [("display", "console")])
