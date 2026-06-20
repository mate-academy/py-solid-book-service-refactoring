from abc import ABC, abstractmethod


class BaseDisplayer(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class ConsoleDisplayer(BaseDisplayer):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplayer(BaseDisplayer):
    def display(self, content: str) -> None:
        print(content[::-1])


DISPLAYERS = {
    "console": ConsoleDisplayer(),
    "reverse": ReverseDisplayer()
}
