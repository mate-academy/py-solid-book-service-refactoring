from app.display_strategies import (
    DisplayStrategy,
    ConsoleDisplay,
    ReverseDisplay,
)
from app.printer_strategies import (
    PrinterStrategy,
    ConsolePrinter,
    ReversePrinter,
)
from app.serializers import (
    SerializerStrategy,
    JsonSerializer,
    XmlSerializer,
)


class StrategyFactory:
    _display_strategies: dict[str, DisplayStrategy] = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }
    _print_strategies: dict[str, PrinterStrategy] = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter(),
    }
    _serialize_strategies: dict[str, SerializerStrategy] = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }

    @classmethod
    def get_display(cls, method_type: str) -> DisplayStrategy:
        if method_type not in cls._display_strategies:
            raise ValueError(f"Unknown display type: {method_type}")
        return cls._display_strategies[method_type]

    @classmethod
    def get_print(cls, method_type: str) -> PrinterStrategy:
        if method_type not in cls._print_strategies:
            raise ValueError(f"Unknown print type: {method_type}")
        return cls._print_strategies[method_type]

    @classmethod
    def get_serialize(cls, method_type: str) -> SerializerStrategy:
        if method_type not in cls._serialize_strategies:
            raise ValueError(f"Unknown serialize type: {method_type}")
        return cls._serialize_strategies[method_type]
