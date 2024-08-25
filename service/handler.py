from abc import ABC, abstractmethod


class OutputBookHandler(ABC):
    @abstractmethod
    def output(self, title: str, content: str) -> any:
        pass


class DisplayOutput(OutputBookHandler):
    def output(self, title: str, content: str) -> any:
        print(f"Printing the book: {title}...")
        print(content)


class PrintOutput(OutputBookHandler):
    def output(self, title: str, content: str) -> any:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])
