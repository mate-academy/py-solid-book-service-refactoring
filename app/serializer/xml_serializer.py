import xml.etree.ElementTree as ElementTree

from app.book import Book
from app.serializer.base import BaseSerializer


class XmlSerializer(BaseSerializer):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")

        title = ElementTree.SubElement(root, "title")
        title.text = book.title

        content = ElementTree.SubElement(root, "content")
        content.text = book.content

        return ElementTree.tostring(root, encoding="unicode")
