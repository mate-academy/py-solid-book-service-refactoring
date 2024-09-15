from typing import Type

from app.book.book_services.method_interface import IBookAction
from app.book.book_services.serializer import (
    BookSerializerXML,
    BookSerializerJSON,
)
from app.book.custom_exceptions.serializer_exceptions import (
    UnknownSerializeTypeError
)
from app.book.factories.method_factory_interface import BookMethodFactory


class BookSerializerFactory(BookMethodFactory):
    @staticmethod
    def get_book_method(serialize_type: str) -> Type[IBookAction]:
        match serialize_type:
            case "xml":
                return BookSerializerXML
            case "json":
                return BookSerializerJSON
        raise UnknownSerializeTypeError(serialize_type)
