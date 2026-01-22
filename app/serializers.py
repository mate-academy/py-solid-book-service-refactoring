from __future__ import annotations
import json
import xml.etree.ElementTree as Et
from interfaces import Serializer, BookDTO


class JsonSerializer(Serializer):
    def serialize(self, book: BookDTO) -> str:
        # еквівалентно старому serialize("json")
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    def serialize(self, book: BookDTO) -> str:
        # еквівалентно старому serialize("xml")
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = book.title
        content = Et.SubElement(root, "content")
        content.text = book.content
        return Et.tostring(root, encoding="unicode")
