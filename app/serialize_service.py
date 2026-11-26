from app.book_serialize import Serialize, JsonSerialize, XmlSerialize
from app.exceptions import SerializeTypeError


class SerializeService:
    @staticmethod
    def get_serialize(serialize_type: str) -> Serialize:
        if serialize_type == "json":
            return JsonSerialize()
        elif serialize_type == "xml":
            return XmlSerialize()
        else:
            raise SerializeTypeError(serialize_type)
