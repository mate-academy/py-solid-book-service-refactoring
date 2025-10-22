from abc import abstractmethod
from app.interfaces.book_interface import BookInterface


class BookPrinterInterface(BookInterface):
    @staticmethod
    @abstractmethod
    def print_book(book: "Book") -> None:
        pass

