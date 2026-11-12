import json

from app.models import Book
from app.serializers.base import Serializer


class JsonSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})
