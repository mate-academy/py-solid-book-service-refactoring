import json
from abc import ABC, abstractmethod
from xml.etree import ElementTree  # noqa: N817

from app.base import Base


class Serializer(ABC, Base):
    @abstractmethod
    def serialize(self) -> str:
        pass


class JSONSerializer(Serializer):
    def serialize(self) -> str:
        return json.dumps(
            {
                "title": self.book.title,
                "content": self.book.content
            }
        )


class XMLSerializer(Serializer):
    def serialize(self) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.book.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.book.content
        return ElementTree.tostring(root, encoding="unicode")
