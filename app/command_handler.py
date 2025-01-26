from typing import Optional, NoReturn

from app.book import Book
from app.commands import Display, PrintBook, Serializer
from app.strategies import JSONSerializer, Console, Reverse, XMLSerializer


class Command:
    def __init__(self) -> None:
        self.allowed_commands = {
            "display": "display",
            "print": "print",
            "serialize": "serialization",
        }
        self.display_strategies = {"console": Console(), "reverse": Reverse()}
        self.serialization_strategies = {
            "json": JSONSerializer(),
            "xml": XMLSerializer(),
        }

    def create_error_msg(self, action: str, method_type: str) -> str:
        return f"Unknown {self.allowed_commands[action]} type: {method_type}"

    def check_command(
        self, action: str, method_type: str
    ) -> Optional[NoReturn]:
        if action not in self.allowed_commands.keys():
            raise ValueError(f"Unknown command: {action}")

        if (
            action in ("display", "print")
            and method_type not in self.display_strategies.keys()
        ):
            raise ValueError(self.create_error_msg(action, method_type))

        elif (
            action == "serialize"
            and method_type not in self.serialization_strategies.keys()
        ):
            raise ValueError(self.create_error_msg(action, method_type))

    def execute(self, cmd: tuple[str, str], book: Book) -> Optional[str]:
        action, method_type = cmd
        self.check_command(action, method_type)

        if action == "display":
            Display(self.display_strategies[method_type]).action(book)

        elif action == "print":
            PrintBook(self.display_strategies[method_type]).action(book)

        elif action == "serialize":
            return Serializer(
                self.serialization_strategies[method_type]
            ).action(book)

        else:
            raise ValueError(f"Unknown command: {action}")
