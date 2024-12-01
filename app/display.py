from app.interface import IDisplayStrategy


class ConsoleDisplayStrategy(IDisplayStrategy):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplayStrategy(IDisplayStrategy):
    def display(self, content: str) -> None:
        print(content[::-1])
