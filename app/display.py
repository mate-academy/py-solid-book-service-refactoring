from abc import ABC, abstractmethod

from app.book import Book


class DisplayBehavior(ABC):

    @abstractmethod
    def print_display(self, book: Book) -> None:
        raise NotImplementedError


class ConsoleDisplay(DisplayBehavior):

    def print_display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayBehavior):

    def print_display(self, book: Book) -> None:
        print(book.content[::-1])


def create_display_behavior(display_type: str) -> DisplayBehavior:
    if display_type == "console":
        return ConsoleDisplay()
    elif display_type == "reverse":
        return ReverseDisplay()
    raise ValueError(f"Unknown display type: {display_type}")
