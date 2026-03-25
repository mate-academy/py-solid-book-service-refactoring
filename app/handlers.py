from app.displayers import DisplayServiceProtocol, PrintServiceProtocol
from app.models import Book


class CommandHandler:
    def __init__(
            self,
            display_service: DisplayServiceProtocol,
            print_service: PrintServiceProtocol,
            serializers: dict
    ) -> None:
        self.display_service = display_service
        self.print_service = print_service
        self.serializer_methods = serializers

        self.display_methods = {
            "console": self.display_service.console,
            "reverse": self.display_service.reverse,
        }

        self.print_methods = {
            "console": self.print_service.console,
            "reverse": self.print_service.reverse,
        }

    def handle(
            self,
            book: Book,
            commands: list[tuple[str, str]]
    ) -> None | str:

        for cmd, mode in commands:

            if cmd == "display":
                if mode not in self.display_methods:
                    raise ValueError(f"Unknown display mode: {mode}")
                self.display_methods[mode](book)
            elif cmd == "print":
                if mode not in self.print_methods:
                    raise ValueError(f"Unknown print type: {mode}")
                self.print_methods[mode](book)
            elif cmd == "serialize":
                if mode not in self.serializer_methods:
                    raise ValueError(f"Unknown serialize type: {mode}")
                return self.serializer_methods[mode].serialize(book)
            else:
                raise ValueError(f"Unknown command: {cmd}")
