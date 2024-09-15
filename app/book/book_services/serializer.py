from app.book.book_services.method_interface import IBookAction
from app.book.book import Book

import json
import xml.etree.ElementTree as ElementTree


class BookSerializerJSON(IBookAction):
    @staticmethod
    def method(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class BookSerializerXML(IBookAction):
    @staticmethod
    def method(book: Book) -> str:
        root = ElementTree.Element("book")
        xml_title = ElementTree.SubElement(root, "title")
        xml_title.text = book.title
        xml_content = ElementTree.SubElement(root, "content")
        xml_content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
