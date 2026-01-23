from abc import ABC, abstractmethod
from typing import Any


class Display(ABC):
    @abstractmethod
    def display(self, book: Any) -> None:
        pass


class Print(ABC):
    @abstractmethod
    def print(self, content: Any) -> None:
        pass


class Serializer(ABC):
    @abstractmethod
    def serialize(self, file_type: str, book: Any) -> str:
        pass
