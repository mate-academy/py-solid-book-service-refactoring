from app.outputs import Displayer, Printer


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content
        self.displayer = Displayer(content)
        self.printer = Printer(content, title)

    def display(self, display_type: str) -> None:
        self.displayer.output(display_type)

    def print_book(self, print_type: str) -> None:
        self.printer.extended_output(print_type)
