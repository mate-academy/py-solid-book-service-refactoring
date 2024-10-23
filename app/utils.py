from app.display import Display, ConsoleDisplay, ReverseDisplay
from app.printing import Print, ConsolePrint, ReversePrint
from app.serializers import Serializer, JsonSerializer, XmlSerializer


def get_display_type(method_type: str) -> Display:
    if method_type == "console":
        return ConsoleDisplay()
    elif method_type == "reverse":
        return ReverseDisplay()
    else:
        raise ValueError(f"Unknown display type: {method_type}")


def get_printer(method_type: str) -> Print:
    if method_type == "console":
        return ConsolePrint()
    elif method_type == "reverse":
        return ReversePrint()
    else:
        raise ValueError(f"Unknown print type: {method_type}")


def get_serializer(method_type: str) -> Serializer:
    if method_type == "json":
        return JsonSerializer()
    elif method_type == "xml":
        return XmlSerializer()
    else:
        raise ValueError(f"Unknown serialize type: {method_type}")
