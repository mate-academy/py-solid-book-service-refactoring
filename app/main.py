from app.books import Book
from app.display import ConsoleDisplayService, ReverseDisplayService
from app.print import ConsolePrintService, ReversePrintService
from app.serializer import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    dispatcher = {
        "display": {
            "console": ConsoleDisplayService.display,
            "reverse": ReverseDisplayService.display
        },
        "print": {
            "console": ConsolePrintService.print,
            "reverse": ReversePrintService.print
        },
        "serialize": {
            "json": JsonSerializer.serialize,
            "xml": XmlSerializer.serialize
        }
    }
    for cmd, method_type in commands:
        if cmd in dispatcher:
            if method_type in dispatcher[cmd]:
                return dispatcher[cmd][method_type](book)
            raise ValueError(f"Unknown command {cmd} type {method_type}")
        raise ValueError(f"Unknown command {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
