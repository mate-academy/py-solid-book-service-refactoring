from abc import ABC, abstractmethod


class BookInterface(ABC):
    title: str
    content: str


class DisplayBookInterface(ABC):
    book: BookInterface

    @abstractmethod
    def display(self) -> None:
        pass


class PrintBookInterface(ABC):
    book: BookInterface

    @abstractmethod
    def print_book(self) -> None:
        pass


class SerializeBookInterface(ABC):
    book: BookInterface

    @abstractmethod
    def serialize(self) -> str:
        pass
