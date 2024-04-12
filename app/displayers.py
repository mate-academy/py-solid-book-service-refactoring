from abc import ABC, abstractmethod

from app.book import Book


class Displayer(ABC):

    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplayer(Displayer):

    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplayer(Displayer):

    def display(self, book: Book) -> None:
        print(book.content[::-1])


def display_factor(book: Book, method_type: str) -> None:
    if method_type == "console":
        displayer = ConsoleDisplayer()
        return displayer.display(book)
    elif method_type == "reverse":
        displayer = ReverseDisplayer()
        return displayer.display(book)
    else:
        raise ValueError(f"Unknown display type: {method_type}")
