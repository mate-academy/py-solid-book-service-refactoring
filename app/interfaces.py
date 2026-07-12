from abc import ABC, abstractmethod


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class PrintStrategy(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        pass


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass
