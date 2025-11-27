from app.book import Book
from app.strategies import ConsolePrint, ReversePrint
from app.serializers import JsonSerializer, XmlSerializer


class CommandHandler:

    display_strategies = {
        "console": ConsolePrint(),
        "reverse": ReversePrint(),
    }

    print_strategies = {
        "console": ConsolePrint(),
        "reverse": ReversePrint(),
    }

    serializers = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }

    def execute(self, book: Book, cmd: str, method: str) -> str | None:
        if cmd == "display":
            strategy = self.display_strategies[method]
            strategy.print(book)

        elif cmd == "print":
            strategy = self.print_strategies[method]
            print(book.title)
            strategy.print(book)

        elif cmd == "serialize":
            serializer = self.serializers[method]
            return serializer.serialize(book)

        else:
            raise ValueError(f"Unknown command: {cmd}")
