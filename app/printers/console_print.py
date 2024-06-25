from app.printers.print_strategy import PrintStrategy


class ConsolePrintStrategy(PrintStrategy):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)
