from abc import ABC, abstractmethod


class DisplayContent(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class ConsoleDisplay(DisplayContent):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(DisplayContent):
    def display(self, content: str) -> None:
        print(content[::-1])


def get_display_class(method_type: str) -> DisplayContent:
    if method_type == "console":
        return ConsoleDisplay()
    elif method_type == "reverse":
        return ReverseDisplay()
    else:
        raise ValueError(f"Unknown type method {method_type}")
