from abc import abstractmethod

from app.book import Book


class BookPrinter(Book):
    @abstractmethod
    def print_book(self) -> None:
        ...


class BookConsolePrinter(BookPrinter):
    def print_book(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)


class BookReversePrinter(BookPrinter):
    def print_book(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])
