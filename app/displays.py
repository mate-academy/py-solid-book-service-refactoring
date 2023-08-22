from abc import abstractmethod

from app.book import Book


class Display:
    @abstractmethod
    def perform_display(self, book: Book) -> None:
        pass


class ConsoleDisplay(Display):
    def perform_display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(Display):
    def perform_display(self, book: Book) -> None:
        print(book.content[::-1])
