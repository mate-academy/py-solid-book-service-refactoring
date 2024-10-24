from abc import ABC, abstractmethod

from app.book import Book


class PrintBookStrategy(ABC):

    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrintBookStrategy(PrintBookStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrintBookStrategy(PrintBookStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class PrintBookStrategyHandler:
    def __init__(
        self,
        console_print_book: PrintBookStrategy,
        reverse_print_book: PrintBookStrategy,
    ) -> None:
        self.console_print_book = console_print_book
        self.reverse_print_book = reverse_print_book

    def print_book(self, book: Book, print_type: str) -> None:
        if print_type == "console":
            return self.console_print_book.print_book(book)
        elif print_type == "reverse":
            return self.reverse_print_book.print_book(book)
        else:
            raise ValueError(f"Unknown display type: {print_type}")
