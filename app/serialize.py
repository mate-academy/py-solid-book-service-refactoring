from app.book import Book
import json
import xml.etree.ElementTree as EleTr


class Serialize(Book):

    def do_action(self) -> None:
        raise NotImplementedError("Must override this method")


class SerializeJSON(Serialize):
    def do_action(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})


class SerializeXML(Serialize):
    def do_action(self) -> EleTr:
        root = EleTr.Element("book")
        title = EleTr.SubElement(root, "title")
        title.text = self.title
        content = EleTr.SubElement(root, "content")
        content.text = self.content
        return EleTr.tostring(root, encoding="unicode")
