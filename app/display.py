from abc import ABC, abstractmethod

from app.book import Book


class BookDisplay(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleBookDisplay(BookDisplay):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseBookDisplay(BookDisplay):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class DisplayProceed:
    display_types = {
        "console": ConsoleBookDisplay,
        "reverse": ReverseBookDisplay}

    def display_book(self, display_type: str, book: Book) -> str:
        if display_type in self.display_types:
            return self.display_types[display_type]().display(book)
        raise ValueError(f"Unknown display type: {display_type}")
