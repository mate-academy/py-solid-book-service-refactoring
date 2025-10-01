from __future__ import annotations

from xml.etree import ElementTree

from services.ports import SerializeStrategy, BookLike


class XmlSerializer(SerializeStrategy):
    def serialize(self, book: "BookLike") -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
