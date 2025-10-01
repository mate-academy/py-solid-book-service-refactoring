from __future__ import annotations

from typing import Dict, Optional
from services.ports import DisplayStrategy, PrintStrategy, SerializeStrategy
from services.registries import (
    default_display_registry,
    default_print_registry,
    default_serialize_registry,
)


class Book:
    def __init__(
        self,
        title: str,
        content: str,
        display_strategies: Optional[Dict[str, DisplayStrategy]] = None,
        print_strategies: Optional[Dict[str, PrintStrategy]] = None,
        serialize_strategies: Optional[Dict[str, SerializeStrategy]] = None,
    ) -> None:
        self.title = title
        self.content = content
        self._display_strategies = (display_strategies
                                    or default_display_registry()
                                    )
        self._print_strategies = (print_strategies
                                  or default_print_registry()
                                  )
        self._serialize_strategies = (serialize_strategies
                                      or default_serialize_registry()
                                      )

    def display(self, display_type: str) -> None:
        strategy = self._display_strategies.get(display_type)
        if not strategy:
            raise ValueError(f"Unknown display type: {display_type}")
        strategy.display(self)

    def print_book(self, print_type: str) -> None:
        strategy = self._print_strategies.get(print_type)
        if not strategy:
            raise ValueError(f"Unknown print type: {print_type}")
        strategy.print(self)

    def serialize(self, serialize_type: str) -> str:
        strategy = self._serialize_strategies.get(serialize_type)
        if not strategy:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
        return strategy.serialize(self)
