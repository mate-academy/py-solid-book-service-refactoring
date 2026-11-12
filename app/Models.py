from dataclasses import dataclass


@dataclass
class Book:
    """Лише дані книги (SRP)."""
    title: str
    content: str
