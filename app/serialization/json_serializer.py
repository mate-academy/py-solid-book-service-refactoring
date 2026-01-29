import json

from app.contracts import BookProtocol
from app.serialization.base import Serializer


class JsonSerializer(Serializer):
    def serialize(self, book: BookProtocol) -> str:
        return json.dumps({"title": book.title, "content": book.content})
