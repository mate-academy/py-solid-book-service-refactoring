from abc import ABC, abstractmethod


class Formatter(ABC):
    @abstractmethod
    def format(self, content: str) -> str:
        pass


class SimpleFormatter(Formatter):
    def format(self, content: str) -> str:
        return content


class ReverseFormatter(Formatter):
    def format(self, content: str) -> str:
        return content[::-1]
