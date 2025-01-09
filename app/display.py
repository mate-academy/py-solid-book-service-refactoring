class DisplayStrategy:
    def display(self, content: str) -> None:
        raise NotImplementedError


class ConsoleDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content[::-1])
