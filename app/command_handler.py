from app.book import Book
from app.display import STRATEGIES as DISPLAY_STRATEGIES
from app.print_book import STRATEGIES as PRINT_STRATEGIES
from app.serializer import STRATEGIES as SERIALIZE_STRATEGIES


class CommandHandler:
    def __init__(self) -> None:
        self._commands = {
            "display": (DISPLAY_STRATEGIES, "display"),
            "print": (PRINT_STRATEGIES, "print_book"),
            "serialize": (SERIALIZE_STRATEGIES, "serialize"),
        }

    def handle(
        self, book: Book, cmd: str, method_type: str
    ) -> None | str:
        if cmd not in self._commands:
            return None

        strategies, method_name = self._commands[cmd]

        if method_type not in strategies:
            raise ValueError(
                f"Unknown {cmd} type: {method_type}"
            )

        return getattr(strategies[method_type], method_name)(book)
