from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class Print(ABC):
    @abstractmethod
    def print(self, title: str, content: str) -> None:
        pass


class Serialize(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class ConsolePrint(Print):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrint(Print):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])
