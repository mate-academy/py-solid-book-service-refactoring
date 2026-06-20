from __future__ import annotations
from abc import ABC, abstractmethod


class Displayer(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        raise NotImplementedError


class ConsoleDisplayer(Displayer):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplayer(Displayer):
    def display(self, content: str) -> None:
        print(content[::-1])


def get_displayer(name: str) -> Displayer:
    mapping: dict[str, Displayer] = {
        "console": ConsoleDisplayer(),
        "reverse": ReverseDisplayer(),
    }
    try:
        return mapping[name]
    except KeyError:
        raise ValueError(f"Unknown display type: {name}")
