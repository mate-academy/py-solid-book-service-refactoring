from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class PrintBook(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        pass


class Serializer(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass
