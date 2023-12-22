from app.book import Book
from app.display import DisplayConsole, DisplayReverse
from app.print_book import PrintBookConsole, PrintBookReverse
from app.serialize import SerializeJson, SerializeXml


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    action = {
        "display":
            {
                "console": DisplayConsole.display,
                "reverse": DisplayReverse.display
            },
        "print":
            {
                "console": PrintBookConsole.print_book,
                "reverse": PrintBookReverse.print_book
            },
        "serialize":
            {
                "json": SerializeJson.serialize,
                "xml": SerializeXml.serialize
            }
    }

    for cmd, method_type in commands:
        if cmd in action and method_type in action[cmd]:
            method = action[cmd][method_type]
            return method(book)
        else:
            raise ValueError(f"Unknown method type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
