from abc import ABC, abstractmethod


class OutputStrategy(ABC):
    @abstractmethod
    def render(self, text: str) -> str:
        pass


class ConsoleOutput(OutputStrategy):
    def render(self, text: str) -> str:
        return text


class ReverseOutput(OutputStrategy):
    def render(self, text: str) -> str:
        return text[::-1]
