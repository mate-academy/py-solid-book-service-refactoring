from app.book import Book
from app.display import DisplayConsole, DisplayReverse
from app.print_book import PrintConsole, PrintReverse
from app.serialize import SerializeJson, SerializeXml


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_actions = {
        "console": DisplayConsole(),
        "reverse": DisplayReverse()
    }
    print_actions = {
        "console": PrintConsole(),
        "reverse": PrintReverse()
    }
    serialize_actions = {
        "json": SerializeJson(),
        "xml": SerializeXml()
    }

    action_map = {
        "display": display_actions,
        "print": print_actions,
        "serialize": serialize_actions
    }

    for cmd, method_type in commands:
        if cmd in action_map and method_type in action_map[cmd]:
            if cmd == "display":
                action_map[cmd][method_type].display(book)
            elif cmd == "print":
                action_map[cmd][method_type].print(book)
            elif cmd == "serialize":
                result = action_map[cmd][method_type].serialize(book)
                return result
        else:
            raise ValueError(f"Unknown command or method type: "
                             f"{cmd} {method_type}")


if __name__ == "__main__":
    book = Book("Sample Book", "This is some sample content.")
    main(book, [
        ("display", "console"),
        ("print", "reverse"),
        ("serialize", "json"),
        ("serialize", "xml"),
    ])
