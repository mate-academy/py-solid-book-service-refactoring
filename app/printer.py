from app.interface import IPrintStrategy


class ConsolePrintStrategy(IPrintStrategy):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...\n{content}")


class ReversePrintStrategy(IPrintStrategy):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...\n{content[::-1]}")
