from abc import abstractmethod

from app.book import Book


class BookDisplayer(Book):
    @abstractmethod
    def display(self) -> None:
        ...


class BookConsoleDisplayer(BookDisplayer):
    def display(self) -> None:
        print(self.content)


class BookReverseDisplayer(BookDisplayer):
    def display(self) -> None:
        print(self.content[::-1])
