from abc import ABC, abstractmethod

from app.book_model import Book


class BaseDisplayer(ABC):
    @staticmethod
    @abstractmethod
    def display_instance(instance: type) -> None:
        pass


class BaseConsoleDisplayer(BaseDisplayer):
    @staticmethod
    @abstractmethod
    def display_instance(instance: type) -> None:
        pass


class BaseReverseDisplayer(BaseDisplayer):
    @staticmethod
    @abstractmethod
    def display_instance(instance: type) -> None:
        pass


class BookConsoleDisplayer(BaseConsoleDisplayer):
    @staticmethod
    def display_instance(book: Book) -> None:
        print(book.content)


class BookReverseDisplayer(BaseReverseDisplayer):
    @staticmethod
    def display_instance(book: Book) -> None:
        print(book.content[::-1])
