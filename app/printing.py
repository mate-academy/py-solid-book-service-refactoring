from abc import abstractmethod, ABC

from app.book_model import Book


class BasePrinter(ABC):
    @staticmethod
    @abstractmethod
    def print_instance(instance: type) -> None:
        pass


class BaseConsolePrinter(BasePrinter):
    @staticmethod
    @abstractmethod
    def print_instance(instance: type) -> None:
        pass


class BaseReversePrinter(BasePrinter):
    @staticmethod
    @abstractmethod
    def print_instance(instance: type) -> None:
        pass


class BookConsolePrinter(BaseConsolePrinter):
    @staticmethod
    def print_instance(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class BookReversePrinter(BaseReversePrinter):
    @staticmethod
    def print_instance(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
