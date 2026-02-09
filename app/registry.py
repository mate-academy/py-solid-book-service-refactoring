from app.display.strategies import ConsoleDisplay, ReverseDisplay
from app.printer.strategies import ConsolePrint, ReversePrint
from app.serializers import JSONSerializer, XMLSerializer

STRATEGIES = {
    "display": {
        "console": ConsoleDisplay,
        "reverse": ReverseDisplay,
    },
    "print": {
        "console": ConsolePrint,
        "reverse": ReversePrint,
    },
    "serialize": {
        "json": JSONSerializer,
        "xml": XMLSerializer,
    }
}


def get_strategy(category: str, method_type: str) -> object:
    strategy_class = STRATEGIES.get(category, {}).get(method_type)
    if not strategy_class:
        raise ValueError(f"Unknown {category} type: {method_type}")
    return strategy_class()
