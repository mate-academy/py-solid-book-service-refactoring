from .display import ConsoleDisplay, ReverseDisplay
from .printer import ConsolePrinter, ReversePrinter
from .serializer import JsonSerializer, XmlSerializer


COMMANDS = {
    ("display", "console"): lambda book: ConsoleDisplay().display(book),
    ("display", "reverse"): lambda book: ReverseDisplay().display(book),
    ("print", "console"): lambda book: ConsolePrinter().print(book),
    ("print", "reverse"): lambda book: ReversePrinter().print(book),
    ("serialize", "json"): lambda book: JsonSerializer().serialize(book),
    ("serialize", "xml"): lambda book: XmlSerializer().serialize(book),
}


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd in commands:
        helper = COMMANDS[cmd]
        result = helper(book)
        if cmd[0] == "serialize":
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
