from abc import abstractmethod, ABC


class BookDisplay(ABC):
    @abstractmethod
    def display(self, content: str) -> any:
        pass


class BookDisplayConsole(BookDisplay):
    def display(self, content: str) -> any:
        print(content)


class BookDisplayReverse(BookDisplay):
    def display(self, content: str) -> any:
        print(content[::-1])
