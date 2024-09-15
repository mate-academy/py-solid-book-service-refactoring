from abc import ABC, abstractmethod
from typing import Type

from app.book.book_services.method_interface import IBookAction


class BookMethodFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_book_method(method_type: str) -> Type[IBookAction]:
        pass
