import json
import xml.etree.ElementTree as ETree
from abc import ABC, abstractmethod

from app.books import Base


class BookSerializer(Base, ABC):

    @abstractmethod
    def serialize(self) -> str:
        pass


class JSONSerializer(BookSerializer):

    def serialize(self) -> str:
        return json.dumps(
            {"title": self.book.title, "content": self.book.content}
        )


class XMLSerializer(BookSerializer):

    def serialize(self) -> str:
        root = ETree.Element("book")
        title = ETree.SubElement(root, "title")
        title.text = self.book.title
        content = ETree.SubElement(root, "content")
        content.text = self.book.content
        return ETree.tostring(root, encoding="unicode")
