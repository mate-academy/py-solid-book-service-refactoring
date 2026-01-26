from app.enums import SerializeType
from app.interfaces import HasTitleContent
from app.serializer import SerializeStrategy


class SerializeService:
    def __init__(self,
                 serializers: dict[SerializeType, SerializeStrategy]) -> None:
        self.serializers = serializers

    def serialize(self, book: HasTitleContent, serialize_type: str) -> str:
        st = SerializeType.from_str(serialize_type)
        serializer = self.serializers.get(st)

        if serializer is None:
            raise ValueError(f"No serializer found for type: {serialize_type}")

        return serializer.serialize(book)
