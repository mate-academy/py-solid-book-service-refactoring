from app.printing.base import Printer
from app.printing.console import ConsolePrinter
from app.printing.reverse import ReversePrinter


_PRINTERS: dict[str, type[Printer]] = {
    "console": ConsolePrinter,
    "reverse": ReversePrinter,
}


def get_printer(print_type: str) -> Printer:
    try:
        return _PRINTERS[print_type]()
    except KeyError as exc:
        raise ValueError(f"Unknown print type: {print_type}") from exc
