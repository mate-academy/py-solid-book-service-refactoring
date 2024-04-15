import json
from abc import abstractmethod
import xml.etree.ElementTree as ET # noqa

from app.book import Book


class Serializer:

    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def serialize(self) -> None:
        pass


class JsonSerializer(Serializer):

    def serialize(self) -> str:
        return json.dumps(
            {"title": self.book.title, "content": self.book.content}
        )


class XmlSerializer(Serializer):

    def serialize(self) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.book.title
        content = ET.SubElement(root, "content")
        content.text = self.book.content
        return ET.tostring(root, encoding="unicode")
