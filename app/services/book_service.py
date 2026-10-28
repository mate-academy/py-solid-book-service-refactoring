from app.displayers.displayers import ConsoleDisplayer, ReverseDisplayer
from app.models.book import Book
from app.printers.printers import ConsolePrinter, ReversePrinter
from app.serializers.serializers import JsonSerializer, XmlSerializer


class BookService:
    def __init__(self) -> None:
        self.displayers = {
            "console": ConsoleDisplayer(),
            "reverse": ReverseDisplayer(),
        }
        self.printers = {
            "console": ConsolePrinter(),
            "reverse": ReversePrinter(),
        }
        self.serializers = {
            "json": JsonSerializer(),
            "xml": XmlSerializer(),
        }

    def execute(
        self,
        book: Book,
        commands: list[tuple[str, str]],
    ) -> None | str:
        for command, method_type in commands:
            if command == "display":
                self._run(self.displayers, method_type, "display", book)
            elif command == "print":
                self._run(self.printers, method_type, "print_book", book)
            elif command == "serialize":
                return self._run(
                    self.serializers, method_type, "serialize", book
                )

    @staticmethod
    def _run(handlers: dict, key: str, method: str, book: Book) -> None | str:
        try:
            handler = handlers[key]
        except KeyError as error:
            raise ValueError(f"Unknown {method} type: {key}") from error
        return getattr(handler, method)(book)
