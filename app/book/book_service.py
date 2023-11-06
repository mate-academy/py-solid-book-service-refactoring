from app.datautils.displays import (
    DisplayStrategy,
    ConsoleDisplay,
    ReverseDisplay,
)
from app.book.book import Book
from app.datautils.prints import PrintStrategy, ConsolePrint, ReversePrint
from app.datautils.serializers import (
    SerializerStrategy,
    JsonSerializer,
    XmlSerializer,
)

DISPLAY_STRATEGIES = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay,
}

PRINT_STRATEGIES = {
    "console": ConsolePrint,
    "reverse": ReversePrint,
}

SERIALIZER_STRATEGIES = {
    "json": JsonSerializer,
    "xml": XmlSerializer,
}


class BookService:
    def __init__(
        self,
        book: Book,
        display_strategy: DisplayStrategy = None,
        print_strategy: PrintStrategy = None,
        serializer_strategy: SerializerStrategy = None,
    ) -> None:
        self.book = book
        self.display_strategy = display_strategy
        self.print_strategy = print_strategy
        self.serializer_strategy = serializer_strategy

    @classmethod
    def create_book_service(
        cls, book: Book, cmd: str, method_type: str
    ) -> "BookService":
        if cmd == "display":
            if method_type not in DISPLAY_STRATEGIES:
                raise ValueError(f"Unknown display type: {method_type}")
            display_strategy = DISPLAY_STRATEGIES[method_type](book.content)
            return cls(book, display_strategy=display_strategy)
        elif cmd == "print":
            if method_type not in PRINT_STRATEGIES:
                raise ValueError(f"Unknown print type: {method_type}")
            print_strategy = PRINT_STRATEGIES[method_type](
                book.title, book.content
            )
            return cls(book, print_strategy=print_strategy)
        elif cmd == "serialize":
            if method_type not in SERIALIZER_STRATEGIES:
                raise ValueError(f"Unknown serialize type: {method_type}")
            serializer_strategy = SERIALIZER_STRATEGIES[method_type](
                book.title, book.content
            )
            return cls(book, serializer_strategy=serializer_strategy)

    def operate(self) -> str:
        if self.display_strategy:
            self.display_strategy.display()
        elif self.print_strategy:
            self.print_strategy.print()
        elif self.serializer_strategy:
            return self.serializer_strategy.serialize()
