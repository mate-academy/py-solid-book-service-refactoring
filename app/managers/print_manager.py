from abc import ABC, abstractmethod
from typing import Optional


class PrintManager(ABC):
    def __init__(self) -> None:
        self.title: Optional[str] = None
        self.content: Optional[str] = None

    @abstractmethod
    def print(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class PrintConsole(PrintManager):
    def __init__(self) -> None:
        super().__init__()

    def print(self, title: str, content: str) -> None:
        super().print(title, content)
        print(f"Printing the {self.title}...")
        print(self.content)


class PrintReverse(PrintManager):
    def __init__(self) -> None:
        super().__init__()

    def print(self, title: str, content: str) -> None:
        super().print(title, content)
        print(f"Printing the {self.title} in reverse...")
        print(self.content[::-1])
