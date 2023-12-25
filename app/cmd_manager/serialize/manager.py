from app.cmd_manager.serialize.serializers import (JsonSerializer, Serializer,
                                                   XmlSerializer)
from app.validators import SerializeTypeValidatorMixin


class SerializeManager(SerializeTypeValidatorMixin):
    def set_serializer(self, serialize_type: str) -> Serializer:
        self.validate_type(serialize_type)

        if serialize_type == "json":
            return JsonSerializer()

        if serialize_type == "xml":
            return XmlSerializer()
