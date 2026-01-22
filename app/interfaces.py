from __future__ import annotations
from typing import Protocol
from dataclasses import dataclass


@dataclass(frozen=True)
class BookDTO:
    title: str
    content: str


class DisplayStrategy(Protocol):
    def display(self, book: BookDTO) -> None:
        ...


class PrintStrategy(Protocol):
    def print_book(self, book: BookDTO) -> None:
        ...


class Serializer(Protocol):
    def serialize(self, book: BookDTO) -> str:
        ...
