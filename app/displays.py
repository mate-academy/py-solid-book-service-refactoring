from abc import ABC, abstractmethod

from app.book import Book


class Display(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(Display):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(Display):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


DISPLAYS: dict[str, Display] = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}


def get_display(display_type: str) -> Display:
    display = DISPLAYS.get(display_type)
    if display is None:
        raise ValueError(f"Unknown display type: {display_type}")
    return display
