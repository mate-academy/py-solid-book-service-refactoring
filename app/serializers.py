import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET  # noqa: N817

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
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.book.title
        content = ET.SubElement(root, "content")
        content.text = self.book.content
        return ET.tostring(root, encoding="unicode")
