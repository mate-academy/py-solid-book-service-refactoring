from abc import abstractmethod, ABC


class BookDisplay(ABC):
    def __init__(self, book: any) -> None:
        self.book = book

    @abstractmethod
    def display(self) -> any:
        pass


class BookDisplayConsole(BookDisplay):
    def display(self) -> any:
        print(self.book.content)


class BookDisplayReverse(BookDisplay):
    def display(self) -> any:
        print(self.book.content[::-1])
