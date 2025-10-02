from abc import ABC, abstractmethod

from app.book import Book
from app.displayers import IDisplayer


class IPrinter(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class BookPrinter(IPrinter):
    def __init__(self, displayer: IDisplayer):
        self.displayer = displayer

    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        self.displayer.display(book)
