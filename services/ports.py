from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class BookLike(Protocol):
    title: str
    content: str


class DisplayStrategy(Protocol):
    def display(self, book: "BookLike") -> None:
        ...


class PrintStrategy(Protocol):
    def print(self, book: "BookLike") -> None:
        ...


class SerializeStrategy(Protocol):
    def serialize(self, book: "BookLike") -> str:
        ...
