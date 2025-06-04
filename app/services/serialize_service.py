from ..utils import json_utils, xml_utils


class SerializeService:
    @staticmethod
    def serialize(title: str, content: str, serialize_type: str) -> str:
        if serialize_type == "json":
            return json_utils.to_json(title, content)
        elif serialize_type == "xml":
            return xml_utils.to_xml(title, content)
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
