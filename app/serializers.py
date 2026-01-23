import json
import xml.etree.ElementTree as ElTree
from typing import Any

from app.abstract_models import Serializer


class JsonSerializer(Serializer):
    def serialize(self, book: Any) -> str:
        return json.dumps(
            {
                "title": book.title,
                "content": book.content
            }
        )


class XMLSerializer(Serializer):
    def serialize(self, book: Any) -> str:
        root = ElTree.Element("book")
        title = ElTree.SubElement(root, "title")
        title.text = book.title
        content = ElTree.SubElement(root, "content")
        content.text = book.content
        return ElTree.tostring(root, encoding="unicode")
