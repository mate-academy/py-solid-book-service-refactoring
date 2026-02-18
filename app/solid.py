from abc import abstractmethod, ABC


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class Formatter(ABC):
    @abstractmethod
    def format(self, text: str) -> str:
        pass


class ConsoleFormatter(Formatter):

    def format(self, text: str) -> str:
        return text


class ReverseFormatter(Formatter):

    def format(self, text: str) -> str:
        return text[::-1]
