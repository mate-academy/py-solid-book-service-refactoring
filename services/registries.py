from __future__ import annotations

from typing import Dict
from services.ports import DisplayStrategy, PrintStrategy, SerializeStrategy
from presenters.display_console import ConsoleDisplay
from presenters.display_reverse import ReverseDisplay
from presenters.print_console import ConsolePrint
from presenters.print_reverse import ReversePrint
from serializers.json_serializer import JsonSerializer
from serializers.xml_serializer import XmlSerializer


def default_display_registry() -> Dict[str, DisplayStrategy]:
    return {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }


def default_print_registry() -> Dict[str, PrintStrategy]:
    return {
        "console": ConsolePrint(),
        "reverse": ReversePrint(),
    }


def default_serialize_registry() -> Dict[str, SerializeStrategy]:
    return {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }
