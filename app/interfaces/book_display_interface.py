from abc import abstractmethod

from app.interfaces.book_interface import BookInterface


class BookDisplayInterface(BookInterface):
    @staticmethod
    @abstractmethod
    def display(book: "Book") -> None:
        pass
