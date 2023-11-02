from typing import Callable

from app.books_manager.outputs import BookConsoleOutput, BookReverseOutput
from app.books_manager.serializers import BookJSONSerializer, BookXMLSerializer


class CommandManager:
    performers = {
        "console": BookConsoleOutput(),
        "reverse": BookReverseOutput(),
        "json": BookJSONSerializer(),
        "xml": BookXMLSerializer()
    }

    def __init__(self, cmd: str, method_type: str):
        self.cmd_name = cmd
        self.cmd = cmd if cmd != "print" else "print_book"
        self.method_type = method_type
        self.performer = self.performers.get(self.method_type)

    def get_method(self) -> Callable:
        return getattr(self.performer, self.cmd)

    def get_error(self) -> Exception:
        return ValueError(f"Unknown {self.cmd_name} type: {self.method_type}")
