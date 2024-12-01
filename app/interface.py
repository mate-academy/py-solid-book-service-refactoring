from abc import ABC, abstractmethod


class IDisplayStrategy(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class IPrintStrategy(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        pass


class ISerializer(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass
