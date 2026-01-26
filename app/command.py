from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Tuple, Callable, Optional

from app.book import Book
from app.display import Display, ConsoleDisplay, ReverseDisplay
from app.print import Print, PrintConsole, PrintReverse
from app.serialize import Serialize, JsonSerialize, XmlSerialize


class Command(ABC):
    @abstractmethod
    def execute(self) -> Optional[str]:
        pass


class DisplayCommand(Command):
    def __init__(self, display: Display, book: Book) -> None:
        self.display: Display = display
        self.book: Book = book

    def execute(self) -> None:
        self.display.display(self.book)


class PrintCommand(Command):
    def __init__(self, printer: Print, book: Book) -> None:
        self.printer: Print = printer
        self.book: Book = book

    def execute(self) -> None:
        self.printer.print_book(self.book)


class SerializeCommand(Command):
    def __init__(self, serializer: Serialize, book: Book) -> None:
        self.serializer: Serialize = serializer
        self.book: Book = book

    def execute(self) -> str:
        return self.serializer.serialize(self.book)


class Action(Enum):
    DISPLAY = "display"
    PRINT = "print"
    SERIALIZE = "serialize"


class Mode(Enum):
    CONSOLE = "console"
    REVERSE = "reverse"
    JSON = "json"
    XML = "xml"


COMMAND_FACTORY: Dict[Tuple[Action, Mode], Callable[[Book], Command]] = {
    (Action.DISPLAY, Mode.CONSOLE):
        lambda b: DisplayCommand(ConsoleDisplay(), b),
    (Action.DISPLAY, Mode.REVERSE):
        lambda b: DisplayCommand(ReverseDisplay(), b),
    (Action.PRINT, Mode.CONSOLE):
        lambda b: PrintCommand(PrintConsole(), b),
    (Action.PRINT, Mode.REVERSE):
        lambda b: PrintCommand(PrintReverse(), b),
    (Action.SERIALIZE, Mode.JSON):
        lambda b: SerializeCommand(JsonSerialize(), b),
    (Action.SERIALIZE, Mode.XML):
        lambda b: SerializeCommand(XmlSerialize(), b),
}
