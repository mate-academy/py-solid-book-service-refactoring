from abc import ABC, abstractmethod


class IBook(ABC):
    @property
    @abstractmethod
    def title(self) -> str:
        pass

    @property
    @abstractmethod
    def content(self) -> str:
        pass


class Book(IBook):
    def __init__(self, title: str, content: str) -> None:
        self._title = title
        self._content = content

    @property
    def title(self) -> str:
        return self._title

    @property
    def content(self) -> str:
        return self._content

    @title.setter
    def title(self, value: str) -> None:
        self._title = value

    @content.setter
    def content(self, value: str) -> None:
        self._content = value
