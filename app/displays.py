from abc import ABC, abstractmethod

from app.book import Book


class Display(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(Display):
    def __init__(self, display_type: str) -> None:
        self.display_type = display_type

    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(Display):
    def __init__(self, display_type: str) -> None:
        self.display_type = display_type

    def display(self, book: Book) -> None:
        print(book.content[::-1])


def choose_display_type(display_type: str) -> Display:
    if display_type == "console":
        return ConsoleDisplay(display_type)
    elif display_type == "reverse":
        return ReverseDisplay(display_type)
    else:
        raise ValueError(f"Unknown display type: {display_type}")
