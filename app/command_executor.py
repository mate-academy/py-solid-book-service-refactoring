from collections.abc import Callable
from app.book import Book


class CommandExecutor:
    def __init__(
        self,
        book: Book,
        display_strategies: dict[str, Callable[[Book], None]],
        print_strategies: dict[str, Callable[[Book], None]],
        serializer_strategies: dict[str, Callable[[Book], str]],
    ) -> None:
        self.book = book
        self.display_strategies = display_strategies
        self.print_strategies = print_strategies
        self.serializer_strategies = serializer_strategies

        self.command_map = {
            "display": self._display,
            "print": self._print,
            "serialize": self._serialize,
        }

    def execute(self, command: str, method_type: str) -> str | None:
        try:
            handler = self.command_map[command]
        except KeyError as exc:
            raise ValueError(f"Unknown command: {command}") from exc

        return handler(method_type)

    def _display(self, method_type: str) -> None:
        self.display_strategies[method_type](self.book)
        return None

    def _print(self, method_type: str) -> None:
        self.print_strategies[method_type](self.book)
        return None

    def _serialize(self, method_type: str) -> str:
        return self.serializer_strategies[method_type](self.book)
