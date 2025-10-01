from __future__ import annotations

import json

from services.ports import SerializeStrategy, BookLike


class JsonSerializer(SerializeStrategy):
    def serialize(self, book: "BookLike") -> str:
        return json.dumps({"title": book.title, "content": book.content})
