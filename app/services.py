from app.interfaces import Displayer, Printer, Serializer
from app.models import Book


class CommandProcessor:
    def __init__(
        self,
        displayers: dict[str, Displayer],
        printers: dict[str, Printer],
        serializers: dict[str, Serializer]
    ) -> None:
        self.displayers = displayers
        self.printers = printers
        self.serializers = serializers

    def process(
            self,
            book: Book, commands: list[tuple[str, str]]
    ) -> None | str:
        last_result = None

        for cmd, method_type in commands:
            if cmd == "display":
                if method_type not in self.displayers:
                    raise ValueError(f"Unknown display type: {method_type}")
                self.displayers[method_type].display(book)
            elif cmd == "print":
                if method_type not in self.printers:
                    raise ValueError(f"Unknown print type: {method_type}")
                self.printers[method_type].print(book)
            elif cmd == "serialize":
                if method_type not in self.serializers:
                    raise ValueError(f"Unknown serialize type: {method_type}")
                last_result = self.serializers[method_type].serialize(book)
            else:
                raise ValueError(f"Unknown command: {cmd}")

        return last_result
