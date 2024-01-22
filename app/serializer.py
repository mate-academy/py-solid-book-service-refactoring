from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: object) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, book: object) -> str:
        return json.dumps(
            {
                "title": book.title,
                "content": book.content,
            }
        )


class XmlSerializer(Serializer):
    def serialize(self, book: object) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
