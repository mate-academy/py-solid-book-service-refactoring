from app.commands import DisplayCommand, SerializerCommand, PrintCommand
from app.interfaces import (
    CommandInterface,
    SerializeType, PrintType, DisplayType
)
from app.services import Display, Printer, Serializer


display = Display()
printer = Printer()
serializer = Serializer()


class_commands = {
    "display": DisplayCommand,
    "print": PrintCommand,
    "serialize": SerializerCommand
}


def tuple_to_commands(
        commands: list[tuple[str, str]]
) -> list[CommandInterface]:
    new_commands = []
    for cmd, method_type in commands:
        if cmd in class_commands:

            if cmd == "serialize":
                new_commands.append(SerializerCommand(
                    serializer=serializer,
                    method_type=SerializeType.XML
                    if method_type == "xml" else SerializeType.JSON
                ))
            elif cmd == "print":
                new_commands.append(PrintCommand(
                    printer=printer,
                    method_type=PrintType.CONSOLE
                    if method_type == "console" else PrintType.REVERSE
                ))
            elif cmd == "display":
                new_commands.append(DisplayCommand(
                    display=display,
                    method_type=DisplayType.CONSOLE
                    if method_type == "console" else DisplayType.REVERSE
                ))

    return new_commands
