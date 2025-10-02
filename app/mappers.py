from app.displays import DisplayConsole, DisplayReverse
from app.printers import PrintConsole, PrintReverse
from app.serializers import JsonSerializer, XMLSerializer

DISPLAYS_MAPPER = {
    "console": DisplayConsole,
    "reverse": DisplayReverse,
}

PRINTERS_MAPPER = {
    "console": PrintConsole,
    "reverse": PrintReverse,
}

SERIALIZERS_MAPPER = {
    "json": JsonSerializer,
    "xml": XMLSerializer,
}

COMMANDS_MAPPER = {
    "display": DISPLAYS_MAPPER,
    "print": PRINTERS_MAPPER,
    "serialize": SERIALIZERS_MAPPER,
}
