import json
from app.serializers.serializer_strategy import SerializeStrategy


class JSONSerializeStrategy(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})
