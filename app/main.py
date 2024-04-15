from app.books import Book
from app.display_handlers import ConsoleDisplayHandler, ReverseDisplayHandler
from app.print_handlers import ConsolePrintHandler, ReversePrintHandler
from app.serializers import JSONSerializer, XMLSerializer


ACTIONS = {
    "display": {
        "console": ConsoleDisplayHandler,
        "reverse": ReverseDisplayHandler
    },
    "print": {
        "console": ConsolePrintHandler,
        "reverse": ReversePrintHandler
    },
    "serialize": {
        "json": JSONSerializer,
        "xml": XMLSerializer
    }
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        try:
            if cmd == "display":
                handler = ACTIONS[cmd][method_type]
                handler(book).display()
            elif cmd == "print":
                handler = ACTIONS[cmd][method_type]
                handler(book).print_book()
            elif cmd == "serialize":
                serializer = ACTIONS[cmd][method_type]
                return serializer(book).serialize()
        except KeyError:
            raise ValueError(f"Unknown method type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
