from abc import ABC, abstractmethod

from app.protocols import HasTitleAndContent


class Printer(ABC):
    @staticmethod
    @abstractmethod
    def print(obj: HasTitleAndContent) -> str:
        pass


class BookConsolePrinter(Printer):
    @staticmethod
    def print(obj: HasTitleAndContent) -> str:
        return (
            f"Printing the book: {obj.title}...\n"
            f"{obj.content}"
        )


class BookReversePrinter(Printer):
    @staticmethod
    def print(obj: HasTitleAndContent) -> str:
        return (
            f"Printing the book in reverse: {obj.title}...\n"
            f"{obj.content[::-1]}"
        )
