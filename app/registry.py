from app.displays import ConsoleDisplay, ReverseDisplay
from app.printers import ConsolePrinter, ReverseConsolePrinter
from app.serializers import JsonSerializer, XmlSerializer

STRATEGIES = {
    "display": {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    },
    "print": {
        "console": ConsolePrinter(),
        "reverse": ReverseConsolePrinter(),
    },
    "serialize": {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    },
}
