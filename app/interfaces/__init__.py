"""Interfaces (abstractions) following ISP - segregated interfaces for
each responsibility.
"""

from abc import ABC, abstractmethod


class BookViewer(ABC):
    """Interface for viewing/displaying book content.

    Following ISP: separate interface for viewing only.
    """

    @abstractmethod
    def display(self, book: "Book") -> None:
        """Display the book content."""
        pass


class BookPrinter(ABC):
    """Interface for printing book content.

    Following ISP: separate interface for printing only.
    """

    @abstractmethod
    def print_book(self, book: "Book") -> None:
        """Print the book content."""
        pass


class BookSerializer(ABC):
    """Interface for serializing book content.

    Following ISP: separate interface for serialization only.
    """

    @abstractmethod
    def serialize(self, book: "Book") -> str:
        """Serialize the book to a string representation."""
        pass


# Forward reference for type hints
class Book:
    pass
