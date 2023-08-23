from abc import ABC, abstractmethod


class Print(ABC):
    @abstractmethod
    def print(self, title: str, content: str) -> None:
        pass


class PrintConsole(Print):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the {title}...")
        print(content)


class PrintReverse(Print):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the {title} in reverse...")
        print(content[::-1])
