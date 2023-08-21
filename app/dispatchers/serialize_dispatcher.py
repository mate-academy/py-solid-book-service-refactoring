from __future__ import annotations

from app.entities.book import Book
from app.serializers.serializers import (
    JsonSerializer,
    XmlSerializer
)


class SerializeDispatcher:
    ALLOWED_SERIALIZERS = {
        "json": JsonSerializer,
        "xml": XmlSerializer
    }

    def handle(self, method_type: str, book: Book) -> str | None:
        if self.__is_serialize_type_valid(method_type):
            return self.ALLOWED_SERIALIZERS[method_type](
                book
            ).serialize()
        raise ValueError(f"Unknown serialize type: {method_type}")

    def __is_serialize_type_valid(self, method_type: str) -> bool:
        return method_type in self.ALLOWED_SERIALIZERS
