from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print import ConsolePrintBook, ReversePrintBook
from app.serialize import JsonSerialize, XmlSerialize

ACTIONS = {
    "print": {"console": ConsolePrintBook, "reverse": ReversePrintBook},
    "display": {"console": ConsoleDisplay, "reverse": ReverseDisplay},
    "serialize": {"json": JsonSerialize, "xml": XmlSerialize},
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        try:
            if cmd == "display":
                ACTIONS[cmd][method_type](book).display()

            elif cmd == "print":
                ACTIONS[cmd][method_type](book).print_book()

            elif cmd == "serialize":
                return ACTIONS[cmd][method_type](book).serialize()
        except ValueError as er:
            print("Invalid command!", er)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
