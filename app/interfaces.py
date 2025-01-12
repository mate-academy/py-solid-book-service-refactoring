from abc import ABC, abstractmethod


class BookOperation(ABC):
    """Base interface for book operations."""

    @abstractmethod
    def process(self, content: str, title: str | None = None) -> str | None:
        """Process book content and optionally title."""
