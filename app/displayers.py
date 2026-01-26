from app.formatters import Formatter


class Displayer:
    def __init__(self, formatter: Formatter) -> None:
        self._formatter = formatter

    def display(self, content: str) -> None:
        print(self._formatter.format(content))


class Printer(Displayer):
    def __init__(self, formatter: Formatter) -> None:
        super().__init__(formatter)

    def print(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        self.display(content)
