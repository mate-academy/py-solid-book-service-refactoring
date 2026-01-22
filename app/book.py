from __future__ import annotations
from dataclasses import dataclass
from interfaces import BookDTO
from registries import DISPLAY_REGISTRY, PRINT_REGISTRY, SERIALIZER_REGISTRY


@dataclass
class Book:
    title: str
    content: str

    # Фасадні методи зберігають попередні сигнатури та тексти помилок
    def display(self, display_type: str) -> None:
        strategy = DISPLAY_REGISTRY.get(display_type)
        if strategy is None:
            # Повністю зберігаємо текст помилки
            raise ValueError(f"Unknown display type: {display_type}")
        strategy.display(BookDTO(self.title, self.content))

    def print_book(self, print_type: str) -> None:
        strategy = PRINT_REGISTRY.get(print_type)
        if strategy is None:
            raise ValueError(f"Unknown print type: {print_type}")
        strategy.print_book(BookDTO(self.title, self.content))

    def serialize(self, serialize_type: str) -> str:
        strategy = SERIALIZER_REGISTRY.get(serialize_type)
        if strategy is None:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
        return strategy.serialize(BookDTO(self.title, self.content))
