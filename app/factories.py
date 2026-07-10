from app.display.console import ConsoleDisplayHandler
from app.display.reverse import ReverseDisplayHandler
from app.printer.console import ConsolePrinter
from app.printer.reverse import ReversePrinter
from app.serializer.json_serializer import JsonSerializer
from app.serializer.xml_serializer import XmlSerializer

SERIALIZERS = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
}

DISPLAY_HANDLERS = {
    "console": ConsoleDisplayHandler(),
    "reverse": ReverseDisplayHandler(),
}

PRINTERS = {
    "console": ConsolePrinter(),
    "reverse": ReversePrinter(),
}
