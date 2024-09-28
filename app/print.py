from abc import ABC, abstractmethod


class Print(ABC):
    @abstractmethod
    def print_entity(self, context: dict) -> None:
        """
        Should print entity with given context.
        Title or article's name should be named like 'heading'.
        Other information should be named like 'text'.
        Returns: None

        """

    @abstractmethod
    def _print_heading(self, heading: str) -> None:
        """
        Prints heading of the whole context
        Args:
            heading: str

        Returns: None

        """

    @abstractmethod
    def _print_text(self, text: str) -> None:
        """
        Prints text without heading
        Args:
            text: str

        Returns: None

        """


class ConsolePrint(Print):
    def print_entity(self, context: dict) -> None:
        self._print_heading(context["heading"])
        self._print_text(context["text"])

    def _print_heading(self, heading: str) -> None:
        print(f"Printing the book: {heading}...")

    def _print_text(self, text: str) -> None:
        print(text)


class ReversePrint(Print):
    def print_entity(self, context: dict) -> None:
        self._print_heading(context["heading"])
        self._print_text(context["text"])

    def _print_heading(self, heading: str) -> None:
        print(f"Printing the book in reverse: {heading}...")

    def _print_text(self, text: str) -> None:
        print(text[::-1])
