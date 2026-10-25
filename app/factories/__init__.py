"""Factories for creating view and serializer instances - following
DIP and OCP.

Factories encapsulate object creation logic, allowing new types to be added
without modifying existing code (Open-Closed Principle).
High-level modules depend on factory abstractions, not concrete classes
(Dependency Inversion).
"""

from app.interfaces import BookViewer, BookPrinter, BookSerializer
from app.views import (
    ConsoleBookViewer,
    ReverseBookViewer,
    ConsoleBookPrinter,
    ReverseBookPrinter,
)
from app.serializers import JSONBookSerializer, XMLBookSerializer


class ViewerFactory:
    """Factory for creating BookViewer instances."""

    _viewers: dict[str, type[BookViewer]] = {
        "console": ConsoleBookViewer,
        "reverse": ReverseBookViewer,
    }

    @classmethod
    def register(cls, name: str, viewer_class: type[BookViewer]) -> None:
        """Register a new viewer type (OCP - extend without modifying)."""
        cls._viewers[name] = viewer_class

    @classmethod
    def create(cls, name: str) -> BookViewer:
        """Create a viewer instance by name."""
        if name not in cls._viewers:
            raise ValueError(f"Unknown viewer type: {name}")
        return cls._viewers[name]()


class PrinterFactory:
    """Factory for creating BookPrinter instances."""

    _printers: dict[str, type[BookPrinter]] = {
        "console": ConsoleBookPrinter,
        "reverse": ReverseBookPrinter,
    }

    @classmethod
    def register(cls, name: str, printer_class: type[BookPrinter]) -> None:
        """Register a new printer type (OCP - extend without modifying)."""
        cls._printers[name] = printer_class

    @classmethod
    def create(cls, name: str) -> BookPrinter:
        """Create a printer instance by name."""
        if name not in cls._printers:
            raise ValueError(f"Unknown printer type: {name}")
        return cls._printers[name]()


class SerializerFactory:
    """Factory for creating BookSerializer instances."""

    _serializers: dict[str, type[BookSerializer]] = {
        "json": JSONBookSerializer,
        "xml": XMLBookSerializer,
    }

    @classmethod
    def register(
        cls, name: str, serializer_class: type[BookSerializer]
    ) -> None:
        """Register a new serializer type (OCP - extend without
        modifying)."""
        cls._serializers[name] = serializer_class

    @classmethod
    def create(cls, name: str) -> BookSerializer:
        """Create a serializer instance by name."""
        if name not in cls._serializers:
            raise ValueError(f"Unknown serializer type: {name}")
        return cls._serializers[name]()
