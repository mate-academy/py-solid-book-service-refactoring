import json
from xml.etree import ElementTree
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def get_content(self) -> str:
        return self.content

    def get_title(self) -> str:
        return self.title


class Formatter(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def response_on_command(self, command: str) -> None:
        pass


class ConsoleFormatter(Formatter):
    def response_on_command(self, command: str) -> None:
        if command == "display":
            print(self.book.content)
        elif command == "print":
            print(f"Printing the book: {self.book.title}...")
            print(self.book.content)


class ReverseFormatter(Formatter):
    def response_on_command(self, command: str) -> None:
        if command == "display":
            print(self.book.content[::-1])
        elif command == "print":
            print(f"Printing the book in reverse: {self.book.title}...")
            print(self.book.content[::-1])


class BookFormatter:
    def __init__(self, book: Book) -> None:
        self.book = book
        self.formatters = {
            "console": ConsoleFormatter(self.book),
            "reverse": ReverseFormatter(self.book)
        }

    def formate(self, command: str, action: str) -> None:
        if command in self.formatters:
            formatter = self.formatters[command]
            formatter.response_on_command(action)
        else:
            raise ValueError("Wrong command")


class Serializer(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def serialize(self) -> str:
        pass


class JSONSerializer(Serializer):
    def serialize(self) -> str:
        return json.dumps({
            "title": self.book.title,
            "content": self.book.content
        })


class XMLSerializer(Serializer):
    def serialize(self) -> str:
        root = ElementTree.Element("book")
        title_element = ElementTree.SubElement(root, "title")
        title_element.text = self.book.title
        content_element = ElementTree.SubElement(root, "content")
        content_element.text = self.book.content
        return ElementTree.tostring(root, encoding="unicode")


class BookSerializer:
    def __init__(self, book: Book) -> None:
        self.book = book
        self.serializers = {
            "json": JSONSerializer(self.book),
            "xml": XMLSerializer(self.book)
        }

    def serialize_from_commands(self, command: str) -> str:
        if command in self.serializers:
            serializer = self.serializers[command]
            return serializer.serialize()
        else:
            raise ValueError("Wrong Command")
