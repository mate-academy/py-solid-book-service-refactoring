from abc import abstractmethod
from app.interfaces.book_interface import BookInterface


class BookSerializerInterface(BookInterface):
    @staticmethod
    @abstractmethod
    def serialize(book: "Book") -> str:
        pass
