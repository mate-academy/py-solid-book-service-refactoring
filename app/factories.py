from app.display import DisplayStrategy, ReverseDisplay, ConsoleDisplay
from app.printer import PrintStrategy, ReversePrinter, ConsolePrinter
from app.serializer import SerializerStrategy, JsonSerializer, XMLSerializer


def get_display(display_type: str) -> DisplayStrategy:
    if display_type == "reverse":
        return ReverseDisplay()
    elif display_type == "console":
        return ConsoleDisplay()
    else:
        raise ValueError(f"Unknown display type: {display_type}")


def get_printer(printer_type: str) -> PrintStrategy:
    if printer_type == "reverse":
        display = ReverseDisplay()
        return ReversePrinter(display)
    elif printer_type == "console":
        display = ConsoleDisplay()
        return ConsolePrinter(display)
    else:
        raise ValueError(f"Unknown printer type: {printer_type}")


def get_serializer(serializer_type: str) -> SerializerStrategy:
    if serializer_type == "json":
        return JsonSerializer()
    elif serializer_type == "xml":
        return XMLSerializer()
    else:
        raise ValueError(f"Unknown printer type: {serializer_type}")
