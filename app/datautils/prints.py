from abc import ABC, abstractmethod


class PrintStrategy(ABC):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    @abstractmethod
    def print(self) -> None:
        pass


class ConsolePrint(PrintStrategy):
    def print(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)


class ReversePrint(PrintStrategy):
    def print(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])
