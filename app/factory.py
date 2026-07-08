from app.commands import DisplayCommand, PrintCommand, SerializeCommand
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrinter, ReversePrinter
from app.serializer import JsonSerialize, XmlSerialize


class CommandFactory:
    @staticmethod
    def create(
            cmd: str,
            method_type: str
    ) -> DisplayCommand | PrintCommand | SerializeCommand:
        if cmd == "display":
            display = {
                "console": ConsoleDisplay(),
                "reverse": ReverseDisplay()
            }
            return DisplayCommand(display[method_type])
        elif cmd == "print":
            printers = {
                "console": ConsolePrinter(),
                "reverse": ReversePrinter()
            }
            return PrintCommand(printers[method_type])
        elif cmd == "serialize":
            serialize = {
                "json": JsonSerialize(),
                "xml": XmlSerialize()
            }
            return SerializeCommand(serialize[method_type])
        raise ValueError(f"Unknown command: {cmd}")

