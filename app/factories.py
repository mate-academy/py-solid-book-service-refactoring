from app.interfaces import BookDisplayInterface, BookPrintInterface, BookSerializeInterface
from app.strategies import DISPLAY_STRATEGIES, PRINT_STRATEGIES, SERIALIZE_STRATEGIES


# Functions for process book strategies
def get_display_strategy(name: str) -> BookDisplayInterface:
    try:
        return DISPLAY_STRATEGIES[name]()
    except KeyError:
        raise ValueError(f"Unknown display strategy: {name}")


def get_print_strategy(name: str) -> BookPrintInterface:
    try:
        return PRINT_STRATEGIES[name]()
    except KeyError:
        raise ValueError(f"Unknown print strategy: {name}")


def get_serialize_strategy(name: str) -> BookSerializeInterface:
    try:
        return SERIALIZE_STRATEGIES[name]()
    except KeyError:
        raise ValueError(f"Unknown serialize strategy: {name}")
