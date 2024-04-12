import json
import xml.etree.ElementTree as ET

from abc import ABC, abstractmethod


class BookSerializer(ABC):

    @abstractmethod
    def serialize(self, book_title: str, book_content: str) -> str:
        pass


class JsonSerializer(BookSerializer):

    def serialize(self, book_title: str, book_content: str) -> str:
        return json.dumps({"title": book_title, "content": book_content})


class XMLSerializer(BookSerializer):

    def serialize(self, book_title: str, book_content: str) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book_title
        content = ET.SubElement(root, "content")
        content.text = book_content
        return ET.tostring(root, encoding="unicode")
