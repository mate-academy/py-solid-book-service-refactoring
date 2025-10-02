from typing import Dict, Optional
from app.models import Book
from app.display import DisplayStrategy
from app.printer import PrintStrategy
from app.serializers import Serializer


from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrint, ReversePrint
from app.serializers import JsonSerializer, XmlSerializer


class BookService:
    def __init__(
        self,
        book: Book,
        display_strategies: Optional[Dict[str, DisplayStrategy]] = None,
        print_strategies: Optional[Dict[str, PrintStrategy]] = None,
        serializers: Optional[Dict[str, Serializer]] = None,
    ) -> None:
        self.book = book

        if display_strategies is None:
            display_strategies = {
                "console": ConsoleDisplay(),
                "reverse": ReverseDisplay(),
            }
        if print_strategies is None:
            print_strategies = {
                "console": ConsolePrint(),
                "reverse": ReversePrint(),
            }
        if serializers is None:
            serializers = {
                "json": JsonSerializer(),
                "xml": XmlSerializer(),
            }

        self.display_strategies: Dict[str, DisplayStrategy] = (
            display_strategies
        )
        self.print_strategies: Dict[str, PrintStrategy] = (
            print_strategies
        )
        self.serializers: Dict[str, Serializer] = (
            serializers
        )

    def execute(self, cmd: str, method_type: str) -> None | str:
        if cmd == "display":
            self.display_strategies[method_type].display(self.book)
        elif cmd == "print":
            self.print_strategies[method_type].print_book(self.book)
        elif cmd == "serialize":
            return self.serializers[method_type].serialize(self.book)
        else:
            raise ValueError(f"Unknown command: {cmd}")
