from app.book.book_services.serializer import (
    Serializer,
    SerializerJSON,
    SerializerXML
)
from app.book.custom_exceptions.serializer_errors import (
    UnknownSerializeTypeError
)


class SerializerFactory:
    @staticmethod
    def get_serializer(serialize_type: str) -> Serializer:
        if serialize_type == "json":
            return SerializerJSON()
        elif serialize_type == "xml":
            return SerializerXML()
        else:
            raise UnknownSerializeTypeError(serialize_type)
