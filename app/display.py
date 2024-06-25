from abc import ABC, abstractmethod


class DisplayInterface(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        raise NotImplementedError


class ConsoleDisplay(DisplayInterface):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(DisplayInterface):
    def display(self, content: str) -> None:
        print(content[::-1])


class DisplayService:
    allowed_display_types = {
        "console": ConsoleDisplay,
        "reverse": ReverseDisplay
    }

    def _is_display_type_valid(self, display_type: str) -> bool:
        return display_type in self.allowed_display_types

    def handle_display(self, display_type: str, content: str) -> None:
        if self._is_display_type_valid("console"):
            self.allowed_display_types[display_type]().display(content)
        else:
            raise ValueError(f"Unknown display type: {display_type}")
