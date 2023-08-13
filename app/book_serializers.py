import json
import xml.etree.ElementTree as ElementTree
from abc import abstractmethod

from app.book import Book


class BookSerializer(Book):
    @abstractmethod
    def serialize(self) -> str:
        ...


class BookJSONSerializer(BookSerializer):
    def serialize(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})


class BookXMLSerializer(BookSerializer):
    def serialize(self) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.content
        return ElementTree.tostring(root, encoding="unicode")
