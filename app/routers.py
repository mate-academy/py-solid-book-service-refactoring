from app.displayers import ConsoleDisplayer, ReverseDisplayer, BookDisplayer
from app.printers import ConsolePrinter, ReversePrinter, BookPrinter
from app.serializers import JSONSerializer, XMLSerializer, BookSerializer

DISPLAYERS = {
    "console": ConsoleDisplayer,
    "reverse": ReverseDisplayer
}

PRINTERS = {
    "console": ConsolePrinter,
    "reverse": ReversePrinter
}

SERIALIZERS = {
    "json": JSONSerializer,
    "xml": XMLSerializer
}


def get_displayer(display_type: str) -> BookDisplayer:
    return DISPLAYERS[display_type]()


def get_printer(print_type: str) -> BookPrinter:
    return PRINTERS[print_type]()


def get_serializer(serializer_type: str) -> BookSerializer:
    return SERIALIZERS[serializer_type]()
