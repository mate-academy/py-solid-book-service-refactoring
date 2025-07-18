import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod


# Abstract book interfaces
class BookDisplayInterface(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class BookPrintInterface(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        pass


class BookSerializeInterface(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


# Concrete implementations for different book-related actions
class DisplayConsole(BookDisplayInterface):
    def display(self, content: str) -> None:
        print(content)


class DisplayReverse(BookDisplayInterface):
    def display(self, content: str) -> None:
        print(content[::-1])


class PrintConsole(BookPrintInterface):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class PrintReverse(BookPrintInterface):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


class SerializeJson(BookSerializeInterface):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class SerializeXml(BookSerializeInterface):
    def serialize(self, title: str, content: str) -> str:
        root = ElementTree.Element("book")
        title_elem = ElementTree.SubElement(root, "title")
        title_elem.text = title
        content_elem = ElementTree.SubElement(root, "content")
        content_elem.text = content
        return ElementTree.tostring(root, encoding="unicode")
