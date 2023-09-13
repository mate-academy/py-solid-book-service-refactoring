import json
import xml.etree.ElementTree as ET
from abc import abstractmethod


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    @abstractmethod
    def display(self) -> None:
        ...

    @abstractmethod
    def print_book(self) -> None:
        ...

    @abstractmethod
    def serialize(self) -> str:
        ...

    @property
    def data(self) -> dict:
        return {"title": self.title, "content": self.content}


class BookReverseJson(Book):

    def display(self) -> None:
        print(self.content[::-1])

    def print_book(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])

    def serialize(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})


class BookConsoleXml(Book):

    def display(self) -> None:
        print(self.content)

    def print_book(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)

    def serialize(self) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.title
        content = ET.SubElement(root, "content")
        content.text = self.content
        return ET.tostring(root, encoding="unicode")
