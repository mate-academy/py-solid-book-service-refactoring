from abc import (
    abstractmethod,
    ABC
)

from book.book import Book


class Display(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class DisplayConsole(Display):
    def display(self, book: Book) -> None:
        print(book.content)


class DisplayReverse(Display):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class DisplayBook:
    _strategies = {
        "console": DisplayConsole(),
        "reverse": DisplayReverse(),
    }

    @staticmethod
    def display(book: Book, display_type: str) -> None:
        display_strategy = DisplayBook._strategies.get(display_type)
        if display_strategy is None:
            raise ValueError(f"Unknown display type: {display_type}")
        return display_strategy.display(book)


