from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass

    @staticmethod
    def get_display_class(given_type: str) -> "Display":
        if given_type == "console":
            return ConsoleDisplay

        elif given_type == "reverse":
            return ReversedDisplay

        else:
            raise ValueError(f"Unknown display type: {given_type}")


class ConsoleDisplay(Display):
    def display(self, content: str) -> None:
        print(content)


class ReversedDisplay(Display):
    def display(self, content: str) -> None:
        print(content[::-1])
