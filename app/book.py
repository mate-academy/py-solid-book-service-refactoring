from abc import ABC, abstractmethod


class BookABC(ABC):
    @property
    @abstractmethod
    def title() -> str:
        pass

    @property
    @abstractmethod
    def content() -> str:
        pass
