from __future__ import annotations
from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        raise NotImplementedError


class ConsolePrinter(Printer):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrinter(Printer):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


def get_printer(name: str) -> Printer:
    mapping: dict[str, Printer] = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter(),
    }
    try:
        return mapping[name]
    except KeyError:
        raise ValueError(f"Unknown print type: {name}")
