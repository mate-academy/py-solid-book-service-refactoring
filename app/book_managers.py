from app.book import Book
import json
import xml.etree.ElementTree as Et
from abc import ABC, abstractmethod


class BookPrinter(ABC):
    @abstractmethod
    def print(self) -> None:
        pass


class BookConsolePrinter(Book, BookPrinter):
    def __init__(self, title: str, content: str) -> None:
        super().__init__(title, content)

    def print(self) -> None:
        print(f"""Printing the book: {self.title}...
                {self.content}""")


class BookReversePrinter(Book, BookPrinter):
    def __init__(self, title: str, content: str) -> None:
        super().__init__(title, content)

    def print(self) -> None:
        print(f"""Printing the book in reverse: {self.title}...
                {self.content[::-1]}""")


class BookViewer(ABC):
    @abstractmethod
    def display(self) -> None:
        pass


class BookConsoleViewer(Book, BookViewer):
    def __init__(self, title: str, content: str) -> None:
        super().__init__(title, content)

    def display(self) -> None:
        print(self.content)


class BookReverseViewer(Book, BookViewer):
    def __init__(self, title: str, content: str) -> None:
        super().__init__(title, content)

    def display(self) -> None:
        print(self.content[::-1])


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self) -> str:
        pass


class BookJsonSerializer(Book, BookSerializer):
    def __init__(self, title: str, content: str) -> None:
        super().__init__(title, content)

    def serialize(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})


class BookXmlSerializer(Book, BookSerializer):
    def __init__(self, title: str, content: str) -> None:
        super().__init__(title, content)

    def serialize(self) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = self.title
        content = Et.SubElement(root, "content")
        content.text = self.content

        return Et.tostring(root, encoding="unicode")
