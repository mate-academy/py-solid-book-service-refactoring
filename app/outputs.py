from abc import ABC, abstractmethod


class BaseOutput(ABC):
    def __init__(self, content: str):
        self.content = content

    @abstractmethod
    def output(self, display_type):
        pass


class Displayer(BaseOutput):
    def output(self, display_type: str) -> None:
        if display_type == "console":
            print(self.content)
        elif display_type == "reverse":
            print(self.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {display_type}")


class Printer(Displayer):
    def __init__(self, content: str, title: str):
        super().__init__(content)
        self.title = title

    def extended_output(self, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {self.title}...")
            self.output(print_type)
        elif print_type == "reverse":
            print(f"Printing the book in reverse: {self.title}...")
            self.output(print_type)
        else:
            raise ValueError(f"Unknown print type: {print_type}")
