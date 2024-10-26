import json
import xml.etree.ElementTree as ElementTree
from abc import ABC

from app.publications import Publication


class BaseSerializer(ABC):
    def serialize(self, publication: Publication) -> str:
        pass


class JSONSerializer(BaseSerializer):
    def serialize(self, publication: Publication) -> str:
        return json.dumps(
            {
                "title": publication.title,
                "content": publication.content
            }
        )


class XMLSerializer(BaseSerializer):
    def serialize(self, publication: Publication) -> str:
        root = ElementTree.Element(publication.type_name())
        title = ElementTree.SubElement(root, "title")
        title.text = publication.title
        content = ElementTree.SubElement(root, "content")
        content.text = publication.content

        return ElementTree.tostring(root, encoding="unicode")
