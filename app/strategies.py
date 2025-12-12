from .display import ConsoleDisplay, ReverseDisplay
from .printer import ConsolePrinter, ReversePrinter
from .serializer import JsonSerializer, XmlSerializer


DISPLAY_STRATEGIES = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}


PRINTER_STRATEGIES = {
    "console": ConsolePrinter(),
    "reverse": ReversePrinter(),
}


SERIALIZER_STRATEGIES = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
}
