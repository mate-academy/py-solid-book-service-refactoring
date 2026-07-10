from abc import ABC, abstractmethod

from app.book import Book


class DisplayType(ABC, Book):
    @abstractmethod
    def display(self):
        pass


class DisplayConsole(DisplayType):
    def display(self):
        print(self.content)


class DisplayReverse(DisplayType):
    def display(self):
        print(self.content[::-1])
