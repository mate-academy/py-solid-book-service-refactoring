from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print_book import ConsolePrint, ReverserPrint
from app.serializers import JSONSerializer, XMLSerializer


actions = {
    "display": {
        "console": ConsoleDisplay,
        "reverse": ReverseDisplay,
    },
    "print": {
        "console": ConsolePrint,
        "reverse": ReverserPrint,
    },
    "serialize": {
        "json": JSONSerializer,
        "xml": XMLSerializer,
    },
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd in actions and method_type in actions[cmd]:
            action_class = actions[cmd][method_type]

            if cmd == "serialize":
                return action_class.serialize(book)
            else:
                (
                    action_class.display(book)
                    if cmd == "display"
                    else action_class.print_book(book)
                )
        else:
            raise ValueError(f"Unknown combination: {cmd} - {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
