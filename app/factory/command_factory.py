from app.commands.display import DisplayCommand
from app.commands.print import PrintCommand
from app.commands.serialize import SerializeCommand

from app.processors.display import ConsoleDisplay, ReverseDisplay
from app.processors.print import ConsolePrint, ReversePrint
from app.processors.serialize import JsonSerialize, XmlSerialize

from app.commands.base import Command


def command_factory(cmd: str, mode: str) -> Command:
    if cmd == "display":
        if mode == "console":
            return DisplayCommand(ConsoleDisplay())
        if mode == "reverse":
            return DisplayCommand(ReverseDisplay())

    if cmd == "print":
        if mode == "console":
            return PrintCommand(ConsolePrint())
        if mode == "reverse":
            return PrintCommand(ReversePrint())

    if cmd == "serialize":
        if mode == "json":
            return SerializeCommand(JsonSerialize())
        if mode == "xml":
            return SerializeCommand(XmlSerialize())

    raise ValueError(f"Unknown command: {cmd} {mode}")
