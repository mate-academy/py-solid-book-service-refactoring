from app.book import Book
from app.display import ConsoleDisplayBook, ReverseDisplayBook
from app.print import ConsolePrintBook, ReversePrintBook
from app.serializer import JsonBookSerializer, XMLBookSerializer


class BookCommandsManager:
    @classmethod
    def action(
            cls,
            book: Book,
            commands: list[tuple[str, str]]
    ) -> None | str:

        for cmd, method in commands:
            if cmd == "display":
                if method == "console":
                    ConsoleDisplayBook(book).display()
                elif method == "reverse":
                    ReverseDisplayBook(book).display()

            elif cmd == "print":
                if method == "console":
                    ConsolePrintBook(book).print()
                elif method == "reverse":
                    ReversePrintBook(book).print()

            elif cmd == "serialize":
                if method == "json":
                    return JsonBookSerializer(book).serialize()
                elif method == "xml":
                    return XMLBookSerializer(book).serialize()
