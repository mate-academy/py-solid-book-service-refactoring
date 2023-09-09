from abc import ABC, abstractmethod

from app.book import ObjectWithContent


class Printer(ABC):
    def __init__(
            self,
            display_type: str,
            object_to_print: ObjectWithContent
    ) -> None:
        self.display_type = display_type
        self.object_to_print = object_to_print

    @abstractmethod
    def print(self) -> None:
        pass


class SimplePrinter(Printer):
    def __print_console(self) -> None:
        print(
            f"Printing the "
            f"{self.object_to_print.__class__.__name__}: "
            f"{self.object_to_print.title}..."
        )
        print(self.object_to_print.content)

    def __print_reverse(self) -> None:
        print(
            f"Printing the "
            f"{self.object_to_print.__class__.__name__} "
            f"in reverse: {self.object_to_print.title}..."
        )
        print(self.object_to_print.content[::-1])

    def print(self) -> None:
        if self.display_type == "console":
            self.__print_console()
        elif self.display_type == "reverse":
            self.__print_reverse()
