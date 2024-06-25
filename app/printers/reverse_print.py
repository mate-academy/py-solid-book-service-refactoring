from app.printers.print_strategy import PrintStrategy


class ReversePrintStrategy(PrintStrategy):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])
