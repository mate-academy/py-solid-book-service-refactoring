from abc import ABC, abstractmethod


class AbstractPrint(ABC):
    @abstractmethod
    def print(self, title, content):
        pass


class ConsolePrint(AbstractPrint):

    def print(self, title, content):
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrint(AbstractPrint):

    def print(self, title, content):
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])