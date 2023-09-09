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
    def __display_in_console(self) -> None:
        print(self.object_to_display.content)

    def __display_in_reverse(self) -> None:
        print(self.object_to_display.content[::-1])

    def display(self) -> None:
        if self.display_type == "console":
            self.__display_in_console()
        elif self.display_type == "reverse":
            self.__display_in_reverse()
        else:
            raise ValueError(f"Unknown display type: {self.display_type}")
