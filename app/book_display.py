from abc import ABC, abstractmethod


class DisplayBook(ABC):
    @abstractmethod
    def display(self, title: str, content: str) -> None:
        pass


class DisplayBookConsole(DisplayBook):
    def display(self, title: str, content: str) -> None:
        print(content)


class DisplayBookReverse(DisplayBook):
    def display(self, title: str, content: str) -> None:
        print(content[::-1])


BOOK_DISPLAY_PROCESSORS = {
    "console": DisplayBookConsole,
    "reverse": DisplayBookReverse,
}
