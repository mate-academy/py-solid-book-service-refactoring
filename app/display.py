class Display:
    def display(self, content: str) -> None:
        raise ValueError("Unknown display type")


class ConsoleDisplay(Display):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(Display):
    def display(self, content: str) -> None:
        print(content[::-1])