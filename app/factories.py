from app.displayers.base import Displayer
from app.displayers.console import ConsoleDisplayer
from app.displayers.reverse import ReverseDisplayer
from app.printers.base import Printer
from app.printers.console import ConsolePrinter
from app.printers.reverse import ReversePrinter
from app.serializers.base import Serializer
from app.serializers.json_serializer import JsonSerializer
from app.serializers.xml_serializer import XmlSerializer

DISPLAYERS = {
    "console": ConsoleDisplayer,
    "reverse": ReverseDisplayer,
}
PRINTERS = {
    "console": ConsolePrinter,
    "reverse": ReversePrinter,
}
SERIALIZERS = {
    "json": JsonSerializer,
    "xml": XmlSerializer,
}


def get_displayer(method_type: str) -> Displayer:
    return DISPLAYERS[method_type]()


def get_printer(method_type: str) -> Printer:
    return PRINTERS[method_type]()


def get_serializer(method_type: str) -> Serializer:
    return SERIALIZERS[method_type]()
