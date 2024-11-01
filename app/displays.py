from app.serializers import DisplayInterface


class ConsoleDisplay(DisplayInterface):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(DisplayInterface):
    def display(self, content: str) -> None:
        print(content[::-1])
