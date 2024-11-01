from abc import ABC, abstractmethod


class DisplayInterface(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class PrintBookInterface(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        pass


class SerializeInterface(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass
