import json
from xml.etree import ElementTree


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def get_content(self) -> str:
        return self.content

    def get_title(self) -> str:
        return self.title


class Formatter:
    def __init__(self, book: Book) -> None:
        self.book = book
        self.commands = {"display": self.display, "print": self.print_book}

    def check_command(self, command: str) -> bool:
        return command in self.commands

    def display(self) -> None:
        print(self.book.content)

    def print_book(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)

    def response_on_command(self, command: str) -> None:
        if self.check_command(command=command):
            return self.commands[command]()


class ConsoleFormatter(Formatter):
    pass


class ReverseFormatter(Formatter):
    def display(self) -> None:
        print(self.book.content[::-1])

    def print_book(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])


class BookFormatter:
    def __init__(self, book: Book) -> None:
        self.book = book
        self.commands = {
            "console": ConsoleFormatter,
            "reverse": ReverseFormatter
        }

    def check_command(self, command: str) -> bool:
        return command in self.commands

    def formate(self, command: str, action: str) -> str:
        if self.check_command(command=command):
            return self.commands[
                command
            ](self.book).response_on_command(action)
        raise ValueError("Wrong command")


class Serializer:
    def __init__(self, book: Book) -> None:
        self.book = book

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
        self.commands = {
            "json": JSONSerializer,
            "xml": XMLSerializer
        }

    def check_command(self, command: str) -> bool:
        return command in self.commands

    def serialize_from_commands(self, command: str) -> None:
        if self.check_command(command):
            return self.commands[command](self.book).serialize()
        raise ValueError("Wrong Command")
