from dataclasses import dataclass


@dataclass(frozen=True)
class Book:
    title: str
    content: str
