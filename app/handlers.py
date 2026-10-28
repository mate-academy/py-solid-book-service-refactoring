from typing import TypeVar

from app.display import (
    DisplayContent,
    ConsoleDisplayContent,
    ReverseDisplayContent,
)
from app.printers import PrintBook, ConsolePrintBook, ReversePrintBook
from app.serializers import SerializeBook, JSONSerializeBook, XMLSerializeBook

DISPLAYS: dict[str, DisplayContent] = {
    "console": ConsoleDisplayContent(),
    "reverse": ReverseDisplayContent(),
}

PRINTERS: dict[str, PrintBook] = {
    "console": ConsolePrintBook(ConsoleDisplayContent()),
    "reverse": ReversePrintBook(ReverseDisplayContent()),
}

SERIALIZERS: dict[str, SerializeBook] = {
    "json": JSONSerializeBook(),
    "xml": XMLSerializeBook(),
}

T = TypeVar("T")


def get_handler(registry: dict[str, T], key: str, kind: str) -> T:
    try:
        return registry[key]
    except KeyError:
        raise ValueError(f"Unknown {kind} type: {key}") from None
