from app.datautils.displays import DisplayStrategy, ConsoleDisplay, ReverseDisplay
from app.book.book import Book
from app.datautils.prints import PrintStrategy, ConsolePrint, ReversePrint
from app.datautils.serializers import SerializerStrategy, JsonSerializer, XmlSerializer

DISPLAY_STRATEGIES = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay,
}

PRINT_STRATEGIES = {
    "console": ConsolePrint(),
    "reverse": ReversePrint(),
}

SERIALIZER_STRATEGIES = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
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

    @staticmethod
    def check_types(cmd: str, method_type: str) -> None:
        if cmd == "display":
            if method_type not in DISPLAY_STRATEGIES:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            if method_type not in PRINT_STRATEGIES:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            if method_type not in SERIALIZER_STRATEGIES:
                raise ValueError(f"Unknown serialize type: {method_type}")

    @classmethod
    def create_book_service(
        cls, book: Book, cmd: str, method_type: str
    ) -> "BookService":
        if cmd == "display":
            display_strategy = DISPLAY_STRATEGIES[method_type](book.content)
            return cls(book, display_strategy=display_strategy)
        elif cmd == "print":
            return cls(book, print_strategy=PRINT_STRATEGIES[method_type])
        elif cmd == "serialize":
            return cls(
                book, serializer_strategy=SERIALIZER_STRATEGIES[method_type]
            )

    def operate(self, operation: str) -> str:
        if operation == "display":
            self.display_strategy.display()
        elif operation == "print":
            self.print_strategy.print(self.book.title, self.book.content)
        elif operation == "serialize":
            return self.serializer_strategy.serialize(
                self.book.title, self.book.content
            )
