from typing import Callable

from app.displays import display_console, display_reverse
from app.printers import print_console, print_reverse
from app.serializers import serialize_json, serialize_xml


DISPLAY_HANDLERS: dict[str, Callable[[str], None]] = {
    "console": display_console,
    "reverse": display_reverse,
}

PRINT_HANDLERS: dict[str, Callable[[str, str], None]] = {
    "console": print_console,
    "reverse": print_reverse,
}

SERIALIZE_HANDLERS: dict[str, Callable[[str, str], str]] = {
    "json": serialize_json,
    "xml": serialize_xml,
}
