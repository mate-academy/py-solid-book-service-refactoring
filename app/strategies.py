from app.display_strategy import ConsoleDisplay, ReverseDisplay
from app.print_strategy import ConsolePrint, ReversePrint
from app.serialization_strategy import JsonSerialization, XmlSerialization

DISPLAY_STRATEGIES = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}

PRINT_STRATEGIES = {
    "console": ConsolePrint(),
    "reverse": ReversePrint(),
}

SERIALIZATION_STRATEGIES = {
    "json": JsonSerialization(),
    "xml": XmlSerialization(),
}
