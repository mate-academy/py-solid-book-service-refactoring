from abc import ABC, abstractmethod

from app.contracts import BookProtocol


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: BookProtocol) -> str:
        raise NotImplementedError
