from abc import ABC, abstractmethod


class PrintStrategy(ABC):
    @abstractmethod
    def print(self, title: str, content: str) -> None:
        pass
