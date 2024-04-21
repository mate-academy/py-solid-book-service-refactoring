from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print_content(self, title: str, content: str) -> None:
        pass


class ConsolePrinter(Printer):
    def __init__(self, content: str = None) -> None:
        self._content = content

    def print_content(self, title: str, content: str = None) -> None:
        if content is None:
            content = self._content
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrinter(Printer):
    def print_content(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])
