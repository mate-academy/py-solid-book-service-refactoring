import json
import xml.etree.ElementTree as ElTr

from app.action import Action
from app.book import Book


class SerializeJson(Action):
    def action(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeXml(Action):
    def action(self, book: Book) -> str:
        root = ElTr.Element("book")
        title = ElTr.SubElement(root, "title")
        title.text = book.title
        content = ElTr.SubElement(root, "content")
        content.text = book.content
        return ElTr.tostring(root, encoding="unicode")
