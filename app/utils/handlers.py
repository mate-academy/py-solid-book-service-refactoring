from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class ConsoleDisplay(Display):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(Display):
    def display(self, content: str) -> None:
        print(content[::-1])


class Print(ABC):
    @abstractmethod
    def print(self, title: str, content: str) -> None:
        pass


class ConsolePrint(Print):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrint(Print):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])
