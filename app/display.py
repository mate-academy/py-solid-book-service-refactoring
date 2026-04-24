from abc import ABC, abstractmethod

from app.models import Book


class DisplayBase(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(DisplayBase):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayBase):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


def get_display(display_type: str) -> DisplayBase:
    if display_type == "console":
        return ConsoleDisplay()
    elif display_type == "reverse":
        return ReverseDisplay()
    else:
        raise ValueError(f"Unknown display type: {display_type}")
