from abc import ABC, abstractmethod


class PrintContent(ABC):
    @abstractmethod
    def print_info(self, title: str, content: str) -> None:
        pass


class ConsolePrint(PrintContent):
    def print_info(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrint(PrintContent):
    def print_info(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


def get_print_class(method_type: str) -> PrintContent:
    if method_type == "console":
        return ConsolePrint()
    elif method_type == "reverse":
        return ReversePrint()
    else:
        raise ValueError(f"Unknown print method {method_type}")
