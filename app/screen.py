from abc import ABC, abstractmethod

from app.book import ObjectWithContent


class Screen(ABC):
    def __init__(
            self,
            display_type: str,
            object_to_display: ObjectWithContent
    ) -> None:
        self.display_type = display_type
        self.object_to_display = object_to_display

    @abstractmethod
    def display(self) -> None:
        pass


class SimpleScreen(Screen):
    DISPLAY_TYPES = {
        "console": "_SimpleScreen__display_in_console",
        "reverse": "_SimpleScreen__display_in_reverse",
    }

    def __display_in_console(self) -> None:
        print(self.object_to_display.content)

    def __display_in_reverse(self) -> None:
        print(self.object_to_display.content[::-1])

    @classmethod
    def get_necessary_display_function(cls, function_key: str) -> callable:
        return cls.__dict__[function_key]

    def display(self) -> None:
        function_key = SimpleScreen.DISPLAY_TYPES.get(self.display_type)
        function = self.get_necessary_display_function(function_key)
        if function:
            function(self)
        else:
            raise ValueError(f"Unknown display type: {self.display_type}")
