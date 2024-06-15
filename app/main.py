from app.book import Book
from app.display import ReverseDisplay, ConsoleDisplay
from app.print_book import ConsolePrintBook, ReversePrintBook
from app.serializer import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_actions = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay()
    }

    print_actions = {
        "console": ConsolePrintBook(),
        "reverse": ReversePrintBook()
    }

    serialize_actions = {
        "json": JsonSerializer(),
        "xml": XmlSerializer()
    }

    result = None
    for cmd, method_type in commands:
        if cmd == "display":
            actions = display_actions.get(method_type)
            if actions:
                book.display(actions)
            else:
                raise ValueError(f"Unknown display type: {method_type}")

        elif cmd == "print":
            actions = print_actions.get(method_type)
            if actions:
                book.print_book(actions)
            else:
                raise ValueError(f"Unknown print type: {method_type}")

        elif cmd == "serialize":
            actions = serialize_actions.get(method_type)
            if actions:
                result = book.serialize(actions)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
