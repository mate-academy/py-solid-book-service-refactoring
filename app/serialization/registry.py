from app.serialization.base import Serializer
from app.serialization.json_serializer import JsonSerializer
from app.serialization.xml_serializer import XmlSerializer


_SERIALIZERS: dict[str, type[Serializer]] = {
    "json": JsonSerializer,
    "xml": XmlSerializer,
}


def get_serializer(serializer_type: str) -> Serializer:
    try:
        return _SERIALIZERS[serializer_type]()
    except KeyError as exc:
        raise ValueError(f"Unknown serialize type: {serializer_type}") from exc
