from abc import ABC, abstractmethod

from app.base import Base


class Printer(ABC, Base):
    @abstractmethod
    def print(self) -> None:
        pass


class ConsolePrinter(Printer):
    def print(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class ReversePrinter(Printer):
    def print(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])
