from abc import ABC, abstractmethod

from app.book import Book


class BookDisplay(ABC):

    @abstractmethod
    def print_display(self, book: Book) -> None:
        pass


class ConsoleBookDisplay(BookDisplay):

    def print_display(self, book: Book) -> None:
        print(book.content)


class ReverseBookDisplay(BookDisplay):

    def print_display(self, book: Book) -> None:
        print(book.content[::-1])


def create_book_displayer(display_type: str) -> BookDisplay:

    if display_type == "console":
        return ConsoleBookDisplay()
    elif display_type == "reverse":
        return ReverseBookDisplay()
    raise ValueError(f"Unknown display type: {display_type}")
