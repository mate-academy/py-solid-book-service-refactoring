from app.book import Book
from app.displayers import ConsoleDisplay, ReverseDisplay
from app.printers import ConsolePrint, ReversePrint
from app.serializers import JsonSerializer, XmlSerializer


COMMANDS = {
    "display": {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay()
    },
    "print": {
        "console": ConsolePrint(),
        "reverse": ReversePrint()
    },
    "serialize": {
        "json": JsonSerializer(),
        "xml": XmlSerializer()
    }
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:

    for cmd, method_type in commands:
        action = COMMANDS.get(cmd).get(method_type)
        if action is None:
            raise ValueError(f"Unknown {cmd} type: {method_type}")
        result = action.execute(book)
        if result:
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
