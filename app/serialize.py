from app.book import Book
import json
import xml.etree.ElementTree as ET


class Serialize(Book):

    def do_action(self):
        raise NotImplementedError("Must override this method")


class SerializeJSON(Serialize):
    def do_action(self):
        return json.dumps({"title": self.title, "content": self.content})


class SerializeXML(Serialize):
    def do_action(self):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.title
        content = ET.SubElement(root, "content")
        content.text = self.content
        return ET.tostring(root, encoding="unicode")
