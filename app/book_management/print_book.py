from abc import ABC, abstractmethod


class Print(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        raise ValueError("Unknown print type")


class ConsolePrint(Print):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrint(Print):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])
