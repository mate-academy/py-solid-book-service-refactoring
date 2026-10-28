import json
import xml.etree.ElementTree as Elect


class SerializeJson:
    def serialize_json(self) -> str:
        return json.dumps({
            "title": self.title,
            "content": self.content,
        })


class SerializeXml:
    def serialize_xml(self) -> str:
        root = Elect.Element("book")
        Elect.SubElement(root, "title").text = self.title
        Elect.SubElement(root, "content").text = self.content
        return Elect.tostring(root, encoding="unicode")
