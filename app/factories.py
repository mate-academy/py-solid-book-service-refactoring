from app.display import BookDisplay, ConsoleDisplay, ReverseDisplay
from app.print import BookPrinter, ConsolePrinter, ReversePrinter
from app.serialize import BookSerializer, JsonBookSerializer, XmlBookSerializer


def display_factory(display_type: str) -> BookDisplay:
    if display_type == "console":
        return ConsoleDisplay()
    elif display_type == "reverse":
        return ReverseDisplay()
    else:
        raise ValueError(f"Unknown display type: {display_type}")


def printer_factory(print_type: str) -> BookPrinter:
    if print_type == "console":
        return ConsolePrinter()
    elif print_type == "reverse":
        return ReversePrinter()
    else:
        raise ValueError(f"Unknown print type: {print_type}")


def serializer_factory(serialize_type: str) -> BookSerializer:
    if serialize_type == "json":
        return JsonBookSerializer()
    elif serialize_type == "xml":
        return XmlBookSerializer()
    else:
        raise ValueError(f"Unknown serialize type: {serialize_type}")
