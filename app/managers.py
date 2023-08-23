from app.book import Book
from app.display import ConsoleDisplayBook, ReverseDisplayBook
from app.print import ConsolePrintBook, ReversePrintBook
from app.serializer import JsonSerializerBook, XMLSerializerBook


class BookCommandManager:
    @classmethod
    def perform_actions(
            cls,
            book: Book,
            commands: list[tuple[str, str]]
    ) -> None | str:

        for cmd, method_type in commands:

            if cmd == "display":
                if method_type == "console":
                    ConsoleDisplayBook(book=book).display()
                elif method_type == "reverse":
                    ReverseDisplayBook(book=book).display()

            elif cmd == "print":
                if method_type == "console":
                    ConsolePrintBook(book=book).print()
                elif method_type == "reverse":
                    ReversePrintBook(book=book).print()

            elif cmd == "serialize":
                if method_type == "json":
                    return JsonSerializerBook(book=book).serialize()
                elif method_type == "xml":
                    return XMLSerializerBook(book=book).serialize()
