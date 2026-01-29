from abc import ABC, abstractmethod

from app.contracts import BookProtocol


class Displayer(ABC):
    @abstractmethod
    def display(self, book: BookProtocol) -> None:
        raise NotImplementedError
