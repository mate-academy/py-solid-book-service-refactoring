class PrintStrategy:
    def print(self, title: str, content: str) -> None:
        raise NotImplementedError


class ConsolePrint(PrintStrategy):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrint(PrintStrategy):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


def get_print_strategy(print_type: str) -> PrintStrategy:
    if print_type == "console":
        return ConsolePrint()
    if print_type == "reverse":
        return ReversePrint()
    raise ValueError(f"Unknown print type: {print_type}")
