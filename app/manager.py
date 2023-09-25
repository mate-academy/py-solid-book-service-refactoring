from app.display import ConsoleDisplay, ReverseDisplay
from app.print import ConsolePrint, ReversePrint
from app.serializers import JsonSerializer, XmlSerializer

DISPLAY = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay
}

PRINT = {
    "console": ConsolePrint,
    "reverse": ReversePrint
}

SERIALIZE = {
    "json": JsonSerializer,
    "xml": XmlSerializer
}
