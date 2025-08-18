from abc import ABC, abstractmethod


class PrinterInterface(ABC):
    @staticmethod
    @abstractmethod
    def print(content: str, title: str) -> None:
        pass


class PrinterConsole(PrinterInterface):
    @staticmethod
    def print(content: str, title: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class PrinterReverse(PrinterInterface):
    @staticmethod
    def print(content: str, title: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])
