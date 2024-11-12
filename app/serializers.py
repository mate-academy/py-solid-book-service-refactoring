import json
import xml.etree.ElementTree as Et
from abc import ABC, abstractmethod


class Serializer(ABC):
    @abstractmethod
    def serialize(self) -> str:
        pass

    def __init__(self, data: str | object) -> None:
        self.data = data


class ObjToJson(Serializer):
    def serialize(self) -> str:
        return json.dumps(self.data, default=lambda o: o.__dict__)


class ObjToXml(Serializer):
    def serialize(self) -> str:
        name_content = self.data.__class__.__name__.lower()
        root = Et.Element(name_content)
        for key, value in self.data.__dict__.items():
            child = Et.SubElement(root, key)
            child.text = str(value)
        return Et.tostring(root, encoding="unicode")


class NormalPrint(Serializer):
    def serialize(self) -> str:
        return self.data


class ReversePrint(Serializer):
    def serialize(self) -> str:
        return self.data[::-1]


class BasicDisplay(Serializer, ABC):
    def __init__(self, title: str, data: str | object) -> None:
        super().__init__(data)
        self.title = title


class NormalDisplay(BasicDisplay):
    def serialize(self) -> str:
        return f"{self.title}\n{self.data}"


class ReverseDisplay(BasicDisplay):
    def serialize(self) -> str:
        return f"{self.title}\n{self.data}"[::-1]


class GetTypeView(ABC):
    def __init__(self, data: str | object, action_type: str) -> None:
        self.data = data
        self.action_type = action_type

    @abstractmethod
    def command(self) -> str:
        pass


class BaseActionTypes(GetTypeView, ABC):
    action_types = {
        "reverse": ReversePrint,
        "console": NormalPrint
    }


class BaseSerializersTypes(GetTypeView, ABC):
    available_serializers = {
        "json": ObjToJson,
        "xml": ObjToXml
    }


class GetTypeDisplayOrException(BaseActionTypes):
    def command(self) -> str:
        if self.action_type in self.action_types:
            print_class = self.action_types[self.action_type]
            view_instance = print_class(self.data)
            return view_instance.serialize()

        raise ValueError(f"Unknown type: {self.action_type}")


class GetTypePrintOrException(BaseActionTypes):
    def __init__(self, obj_title: str, data: str, action_type: str) -> None:
        super().__init__(data, action_type)
        self.obj_title = obj_title

    def command(self) -> str:
        if self.action_type in self.action_types:
            print_class = self.action_types[self.action_type]
            view_instance = print_class(self.data)
            return f"{self.obj_title}\n{view_instance.serialize()}"

        raise ValueError(f"Unknown type: {self.action_type}")


class GetTypeConvertOrException(BaseSerializersTypes):
    def command(self) -> str:
        if self.action_type in self.available_serializers:
            serializer_class = self.available_serializers[self.action_type]
            serializer_instance = serializer_class(self.data)
            return serializer_instance.serialize()

        raise ValueError(f"Unknown serialize type: {self.action_type}")
