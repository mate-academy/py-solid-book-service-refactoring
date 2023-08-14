from abc import ABC, abstractmethod


class PrintManager(ABC):
    @abstractmethod
    def print(self, title: str, content: str) -> None:
        pass


class PrintConsole(PrintManager):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the {title}...")
        print(content)


class PrintReverse(PrintManager):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the {title} in reverse...")
        print(content[::-1])
