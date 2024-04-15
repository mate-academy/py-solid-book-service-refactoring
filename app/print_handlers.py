from abc import ABC, abstractmethod

from app.books import Base


class PrintHandler(Base, ABC):

    @abstractmethod
    def print_book(self) -> None:
        pass


class ConsolePrintHandler(PrintHandler):

    def print_book(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class ReversePrintHandler(PrintHandler):

    def print_book(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])
