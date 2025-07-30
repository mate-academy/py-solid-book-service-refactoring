from .models import (
    Book,
    Command,
    DisplayStrategy,
    PrintStrategy,
    SerializationStrategy, CommandFactory
)
from .strategies import (
    ConsoleDisplayStrategy,
    ReverseDisplayStrategy,
    ConsolePrintStrategy,
    ReversePrintStrategy,
    JsonSerializationStrategy,
    XmlSerializationStrategy
)


class BookDisplayService:
    def display(self, book: Book, strategy: DisplayStrategy) -> None:
        strategy.display(book.content)


class BookPrintService:
    def print_book(self, book: Book, strategy: PrintStrategy) -> None:
        strategy.print_book(book.title, book.content)


class BookSerializationService:
    def serialize(self, book: Book, strategy: SerializationStrategy) -> str:
        return strategy.serialize(book)


class StrategyFactory:
    _display_strategies = {
        "console": ConsoleDisplayStrategy,
        "reverse": ReverseDisplayStrategy
    }

    _print_strategies = {
        "console": ConsolePrintStrategy,
        "reverse": ReversePrintStrategy
    }

    _serialization_strategies = {
        "json": JsonSerializationStrategy,
        "xml": XmlSerializationStrategy
    }

    @classmethod
    def create_display_strategy(cls, strategy_type: str) -> DisplayStrategy:
        if strategy_type not in cls._display_strategies:
            raise ValueError(f"Unknown display strategy: {strategy_type}")
        return cls._display_strategies[strategy_type]()

    @classmethod
    def create_print_strategy(cls, strategy_type: str) -> PrintStrategy:
        if strategy_type not in cls._print_strategies:
            raise ValueError(f"Unknown print strategy: {strategy_type}")
        return cls._print_strategies[strategy_type]()

    @classmethod
    def create_serialization_strategy(
            cls, strategy_type: str
    ) -> SerializationStrategy:
        if strategy_type not in cls._serialization_strategies:
            raise ValueError(
                f"Unknown serialization strategy: {strategy_type}"
            )
        return cls._serialization_strategies[strategy_type]()


class DisplayCommand(Command):
    def __init__(
            self,
            book: Book,
            display_service: BookDisplayService,
            strategy_type: str
    ) -> None:
        self.book = book
        self.display_service = display_service
        self.strategy = StrategyFactory.create_display_strategy(strategy_type)

    def execute(self) -> None:
        self.display_service.display(self.book, self.strategy)
        return None


class PrintCommand(Command):
    def __init__(
            self,
            book: Book,
            print_service: BookPrintService,
            strategy_type: str
    ) -> None:
        self.book = book
        self.print_service = print_service
        self.strategy = StrategyFactory.create_print_strategy(strategy_type)

    def execute(self) -> None:
        self.print_service.print_book(self.book, self.strategy)
        return None


class SerializeCommand(Command):
    def __init__(
            self,
            book: Book,
            serialization_service: BookSerializationService,
            strategy_type: str
    ) -> None:
        self.book = book
        self.serialization_service = serialization_service
        self.strategy = (
            StrategyFactory.create_serialization_strategy(strategy_type)
        )

    def execute(self) -> str:
        return self.serialization_service.serialize(self.book, self.strategy)


class DisplayCommandFactory(CommandFactory):
    def __init__(self, display_service: BookDisplayService) -> None:
        self.display_service = display_service

    def create_command(self, book: Book, method_type: str) -> Command:
        return DisplayCommand(book, self.display_service, method_type)


class PrintCommandFactory(CommandFactory):
    def __init__(self, print_service: BookPrintService) -> None:
        self.print_service = print_service

    def create_command(self, book: Book, method_type: str) -> Command:
        return PrintCommand(book, self.print_service, method_type)


class SerializeCommandFactory(CommandFactory):
    def __init__(
            self, serialization_service: BookSerializationService
    ) -> None:
        self.serialization_service = serialization_service

    def create_command(self, book: Book, method_type: str) -> Command:
        return SerializeCommand(book, self.serialization_service, method_type)


class BookProcessor:
    def __init__(
            self,
            display_service: BookDisplayService,
            print_service: BookPrintService,
            serialization_service: BookSerializationService
    ) -> None:
        self.display_service = display_service
        self.print_service = print_service
        self.serialization_service = serialization_service
        self.factories = {
            "display": DisplayCommandFactory(self.display_service),
            "print": PrintCommandFactory(self.print_service),
            "serialize": SerializeCommandFactory(self.serialization_service)
        }

    def process_commands(
            self, book: Book, commands: list[tuple[str, str]]
    ) -> str | None:
        result = None
        for cmd, method_type in commands:
            command = self._create_command(book, cmd, method_type)
            result = command.execute()
        return result

    def _create_command(
            self, book: Book, cmd: str, method_type: str
    ) -> Command:
        if cmd not in self.factories:
            raise ValueError(f"Unknown command: {cmd}")
        return self.factories[cmd].create_command(book, method_type)
