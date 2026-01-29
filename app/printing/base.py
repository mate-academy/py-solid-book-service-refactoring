from abc import ABC, abstractmethod

from app.contracts import BookProtocol


class Printer(ABC):
    @abstractmethod
    def print(self, book: BookProtocol) -> None:
        raise NotImplementedError
