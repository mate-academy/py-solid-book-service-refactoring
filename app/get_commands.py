from app.displays import DisplayBookConsole, DisplayBookReverse, Display
from app.prints import PrintBookConsole, PrintBookReverse, Print
from app.serializers import SerializeBookJson, SerializeBookXml, Serialize


def get_printer(cmd: str) -> Print:
    commands = {
        "console": PrintBookConsole(),
        "reverse": PrintBookReverse(),
    }
    return commands[cmd]


def get_display(cmd: str) -> Display:
    commands = {
        "console": DisplayBookConsole(),
        "reverse": DisplayBookReverse(),
    }
    return commands[cmd]


def get_serializer(cmd: str) -> Serialize:
    commands = {
        "json": SerializeBookJson(),
        "xml": SerializeBookXml(),
    }
    return commands[cmd]
