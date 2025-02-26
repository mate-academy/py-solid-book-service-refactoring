from abc import ABC, abstractmethod


# Interfaces for serialization and output
class Serializer(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class Printer(ABC):
    @abstractmethod
    def print(self, title: str, content: str) -> None:
        pass
