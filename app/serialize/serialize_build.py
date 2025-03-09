from app.serialize.serialize_interface import (
    SerializeInterface,
    JsonSerialize,
    XmlSerialize
)


class SerializeBuild:
    @staticmethod
    def serialize_build(serialize_type: str) -> SerializeInterface:
        if serialize_type == "json":
            return JsonSerialize()
        elif serialize_type == "xml":
            return XmlSerialize()
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
