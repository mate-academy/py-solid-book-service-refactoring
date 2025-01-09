class PrintStrategy:
    def print_book(self, title: str, content: str) -> None:
        raise NotImplementedError


class ConsolePrint(PrintStrategy):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrint(PrintStrategy):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])
