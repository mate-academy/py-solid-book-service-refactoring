from app.book import Book
from app.display import DisplayConsole, DisplayReverse
from app.serialize import SerializeJson, SerializeXml
from app.print import PrintConsole, PrintReverse


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_choices = {
        "console": lambda: DisplayConsole().display(book),
        "reverse": lambda: DisplayReverse().display(book)
    }
    serialize_choices = {
        "json": lambda: SerializeJson().serialize(book),
        "xml": lambda: SerializeXml().serialize(book)
    }
    print_choices = {
        "console": lambda: PrintConsole().print_book(book),
        "reverse": lambda : PrintReverse().print_book(book)
    }

    for cmd, method_type in commands:
        try:
            if cmd == "display":
                if method_type in display_choices:
                    display_choices[method_type]()
                else:
                    print(f"Unknown display method: {method_type}")
            elif cmd == "print":
                if method_type in print_choices:
                    print_choices[method_type]()
                else:
                    print(f"Unknown print method: {method_type}")
            elif cmd == "serialize":
                if method_type in serialize_choices:
                    return serialize_choices[method_type]()
                else:
                    print(f"Unknown serialize method: {method_type}")
            else:
                print(f"Unknown command: {cmd}")
        except Exception as e:
            print(f"Error occurred: {e}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
