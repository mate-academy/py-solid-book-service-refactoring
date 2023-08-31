from __future__ import annotations


class SerializeDispatcher:
    def __init__(self, allowed_serializers: dict) -> None:
        self.allowed_serializers = allowed_serializers

    def handle(self, method_type: str) -> str | None:
        if self.__is_serialize_type_valid(method_type):
            return self.allowed_serializers[method_type].serialize()
        raise ValueError(f"Unknown serialize type: {method_type}")

    def __is_serialize_type_valid(self, method_type: str) -> bool:
        return method_type in self.allowed_serializers
