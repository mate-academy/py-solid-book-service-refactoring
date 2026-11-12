from dataclasses import dataclass


__all__ = ["Book"]


@dataclass
class Book:
    title: str
    content: str
