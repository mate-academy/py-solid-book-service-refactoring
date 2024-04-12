from typing import Callable

from app.book_service.display_types import (
    ConsoleDisplayProcessor,
    ReverseDisplayProcessor
)
from app.book_service.print_book_types import (
    ConsolePrintProcessor,
    ReversePrintProcessor
)
from app.book_service.serializers import (
    JSONSerializeProcessor,
    XMLSerializeProcessor
)


def create_display_processor(display_type: str) -> Callable:
    if display_type == "console":
        return ConsoleDisplayProcessor.display

    elif display_type == "reverse":
        return ReverseDisplayProcessor.display

    raise ValueError(f"Unknown display type: {display_type}")


def create_print_processor(print_type: str) -> Callable:
    if print_type == "console":
        return ConsolePrintProcessor.print_book

    elif print_type == "reverse":
        return ReversePrintProcessor.print_book

    raise ValueError(f"Unknown print type: {print_type}")


def create_serialize_processor(serialize_type: str) -> Callable:
    if serialize_type == "json":
        return JSONSerializeProcessor.serialize

    elif serialize_type == "xml":
        return XMLSerializeProcessor.serialize

    raise ValueError(f"Unknown serialize type: {serialize_type}")
