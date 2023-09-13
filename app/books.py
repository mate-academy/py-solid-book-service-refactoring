import json
import xml.etree.ElementTree as EleT
from abc import abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
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
        root = EleT.Element("book")
        title = EleT.SubElement(root, "title")
        title.text = self.title
        content = EleT.SubElement(root, "content")
        content.text = self.content
        return EleT.tostring(root, encoding="unicode")
