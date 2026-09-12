from app.displayers import ConsoleDisplayer, ReverseDisplayer
from app.interfaces import Displayer, Printer, Serializer
from app.printers import ConsolePrinter, ReversePrinter
from app.serializers import JsonSerializer, XmlSerializer


DISPLAYERS: dict[str, Displayer] = {
    "console": ConsoleDisplayer(),
    "reverse": ReverseDisplayer(),
}

PRINTERS: dict[str, Printer] = {
    "console": ConsolePrinter(),
    "reverse": ReversePrinter(),
}

SERIALIZERS: dict[str, Serializer] = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
}


def get_displayer(display_type: str) -> Displayer:
    return DISPLAYERS[display_type]


def get_printer(print_type: str) -> Printer:
    return PRINTERS[print_type]


def get_serializer(serialize_type: str) -> Serializer:
    return SERIALIZERS[serialize_type]
