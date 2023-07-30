from app.utils.handlers import Display


class ConsoleDisplay(Display):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(Display):
    def display(self, content: str) -> None:
        print(content[::-1])
