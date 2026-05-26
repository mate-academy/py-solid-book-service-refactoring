from enum import Enum, auto

from app.display import BaseDisplay, ConsoleDisplay, ReverseDisplay, Viewer
from app.printer import BasePrint, ConsolePrint, ReversePrint, Printer
from app.serializer import (
    BaseSerializer,
    JsonSerializer,
    XmlSerializer,
    Serializer,
)


class ConsoleCommands(str, Enum):
    display = auto()
    print = auto()
    serialize = auto()


class BaseConsoleCommandsType(str, Enum):
    console = auto()
    reverse = auto()


class SerializeCommands(str, Enum):
    json = auto()
    xml = auto()


DISPLAY_MAP: dict[str, BaseDisplay] = {
    BaseConsoleCommandsType.console.name: ConsoleDisplay(),
    BaseConsoleCommandsType.reverse.name: ReverseDisplay(),
}

PRINT_MAP: dict[str, BasePrint] = {
    BaseConsoleCommandsType.console.name: ConsolePrint(),
    BaseConsoleCommandsType.reverse.name: ReversePrint(),
}

SERIALIZE_MAP: dict[str, BaseSerializer] = {
    SerializeCommands.json.name: JsonSerializer(),
    SerializeCommands.xml.name: XmlSerializer(),
}

COMMAND_MAP = {
    ConsoleCommands.display.name: (DISPLAY_MAP, Viewer),
    ConsoleCommands.print.name: (PRINT_MAP, Printer),
    ConsoleCommands.serialize.name: (SERIALIZE_MAP, Serializer),
}
