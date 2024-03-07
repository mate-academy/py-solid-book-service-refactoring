from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def display(self, content):
        pass


class ConsoleDisplay(Display):

    def display(self, content):
        return content


class ReverseDisplay(Display):

    def display(self, content):
        return content[::-1]
