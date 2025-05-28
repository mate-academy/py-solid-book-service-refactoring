from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ElemT

from app.content_render import ContentRenderer


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, renderer: ContentRenderer) -> None:
        renderer.render(self.content)

    def print_book(self, printer: ContentRenderer) -> None:
        print(f"Printing the book: {self.title}...")
        printer.render(self.content)


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = ElemT.Element("book")
        title = ElemT.SubElement(root, "title")
        title.text = book.title
        content = ElemT.SubElement(root, "content")
        content.text = book.content
        return ElemT.tostring(root, encoding="unicode")
