from app.display.base import Displayer
from app.display.console import ConsoleDisplayer
from app.display.reverse import ReverseDisplayer


_DISPLAYERS: dict[str, type[Displayer]] = {
    "console": ConsoleDisplayer,
    "reverse": ReverseDisplayer,
}


def get_displayer(display_type: str) -> Displayer:
    try:
        return _DISPLAYERS[display_type]()
    except KeyError as exc:
        raise ValueError(f"Unknown display type: {display_type}") from exc
