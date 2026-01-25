from app.enums import SerializeType
from app.interfaces import HasTitleContent
from app.serializer import JsonSerializer, XmlSerializer


class SerializeService:
    def serialize(self, book: HasTitleContent, serialize_type: str) -> str:
        st = SerializeType.from_str(serialize_type)
        match st:
            case SerializeType.JSON:
                return JsonSerializer().serialize(book)
            case SerializeType.XML:
                return XmlSerializer().serialize(book)
