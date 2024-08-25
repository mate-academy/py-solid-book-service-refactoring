from abc import ABC, abstractmethod
from display import Display


class OutputBookHandler(ABC):
    @abstractmethod
    def output(self, title: str, content: str, output_type: Display) -> None:
        pass


class DisplayOutput(OutputBookHandler):
    def output(self, title: str, content: str, output_type: Display) -> None:
        print(f"Displaying the book: {title}...")
        output_type.display(content)


class PrintOutput(OutputBookHandler):
    def output(self, title: str, content: str, output_type: Display) -> None:
        print(f"Printing the book: {title}...")
        output_type.display(content)
