from typing import Dict, Type

from app.actions.display import ConsoleDisplay, ReverseDisplay
from app.actions.printers import ConsolePrint, ReversePrint
from app.actions.serializers import JsonSerializer, XMLSerializer
from app.interfaces import ActionInterface


class ActionFactory:
    _registry: Dict[tuple[str, str], Type[ActionInterface]] = {
        ("display", "console"): ConsoleDisplay,
        ("display", "reverse"): ReverseDisplay,
        ("print", "console"): ConsolePrint,
        ("print", "reverse"): ReversePrint,
        ("serialize", "json"): JsonSerializer,
        ("serialize", "xml"): XMLSerializer,
    }

    @classmethod
    def get_action(cls, command: str, method_type: str) -> ActionInterface:
        try:
            action_class = cls._registry[(command, method_type)]
            return action_class()
        except KeyError:
            raise ValueError(f"Unknown action: {command} - {method_type}")
