from abc import ABC, abstractmethod


class BaseDisplayBook(ABC):

    @abstractmethod
    def display(self, display_type: str) -> None:
        pass


class ConsoleDisplayBook(BaseDisplayBook):

    def display(self, display_type: str) -> None:
        if display_type == "console":
            print(self.content)
        else:
            super().display(display_type)


class ReverseDisplayBook(BaseDisplayBook):

    def display(self, display_type: str) -> None:
        if display_type == "reverse":
            print(self.content[::-1])
        else:
            super().display(display_type)


class DisplayBook(ConsoleDisplayBook, ReverseDisplayBook):
    pass
