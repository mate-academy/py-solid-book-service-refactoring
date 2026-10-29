from abc import abstractmethod, ABC

from app.book import Book


class BookDisplayer(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        ...


class ConsoleDisplayer(BookDisplayer):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplayer(BookDisplayer):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
