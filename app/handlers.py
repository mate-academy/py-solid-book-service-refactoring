from .display import ConsoleDisplay, ReverseDisplay
from .printer import ConsolePrinter, ReversePrinter
from .serializers import JsonSerializer, XmlSerializer


DISPLAY_HANDLERS = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}

PRINT_HANDLERS = {
    "console": ConsolePrinter(),
    "reverse": ReversePrinter(),
}

SERIALIZERS = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
}
