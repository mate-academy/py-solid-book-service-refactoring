import abc


class Display(abc.ABC):
    def __init__(self, content: str) -> None:
        self.content = content

    @abc.abstractmethod
    def display(self) -> None:
        ...


class DisplayConsole(Display):
    def display(self) -> None:
        print(self.content)


class DisplayReverse(Display):
    def display(self) -> None:
        print(self.content[::-1])
