import json
import xml.etree.ElementTree as ET  # noqa: N817
from abc import abstractmethod, ABC


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book_title: str, book_content: str) -> str:
        pass


class JSONSerializer(Serializer):
    def serialize(self, book_title: str, book_content: str) -> str:
        return json.dumps({"title": book_title, "content": book_content})


class XMLSerializer(Serializer):
    def serialize(self, book_title: str, book_content: str) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book_title
        content = ET.SubElement(root, "content")
        content.text = book_content
        return ET.tostring(root, encoding="unicode")
