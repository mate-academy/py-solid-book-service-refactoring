import json
from abc import ABC, abstractstaticmethod
import xml.etree.ElementTree as ET


class BookSerializer:
    @abstractstaticmethod
    def serialize(book):
        pass


class JSONBookSerializer:
    @staticmethod
    def serialize(book):
        return json.dumps({"title": book.title, "content": book.content})


class XMLBookSerializer:
    @staticmethod
    def serialize(book):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
