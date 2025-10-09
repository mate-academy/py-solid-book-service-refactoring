import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class Serializer(ABC):
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    @abstractmethod
    def serialize(self):
        pass


class Json(Serializer):
    def serialize(self):
        return json.dumps({"title": self.title, "content": self.content})


class Xml(Serializer):
    def serialize(self):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.title
        content = ET.SubElement(root, "content")
        content.text = self.content
        return ET.tostring(root, encoding="unicode")


class Book(ABC):
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content
    
    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def print_book(self):
        pass

    def serialize(self, serializer: Serializer) -> str:
        return serializer.serialize()


class ConsoleBook(Book):
    def display(self):
        print(self.content)
    
    def print_book(self):
        print(f"Printing the book: {self.title}...")
        print(self.content)


class ReverseBook(Book):
    def display(self):
        print(self.content[::-1])
    
    def print_book(self):
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])


def main(title: str, content: str, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if method_type == "console":
            book = ConsoleBook(title, content)
        else:
            book = ReverseBook(title, content)
        if cmd == "display":
            book.display()
        elif cmd == "print":
            book.print_book()
        elif cmd == "serialize":
            if method_type == "json":
                return book.serialize(Json(title, content))
            elif method_type == "xml":
                return book.serialize(Xml(title, content))


if __name__ == "__main__":
    title = "Sample Book"
    content = "This is some sample content."
    print(main(title, content, [("display", "reverse"), ("serialize", "xml")]))
