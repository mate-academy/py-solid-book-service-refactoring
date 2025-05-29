from abc import ABC, abstractmethod


class IDisplayStrategy(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class IPrintStrategy(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        pass


class ISerializationStrategy(ABC):
    @abstractmethod
    def serialize(self, data: dict) -> str:
        pass
