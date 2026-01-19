import enum
from abc import ABC, abstractmethod

from app.models import Book


class DisplayType(enum.Enum):
    CONSOLE = "console"
    REVERSE = "reverse"


class PrintType(enum.Enum):
    CONSOLE = "console"
    REVERSE = "reverse"


class SerializeType(enum.Enum):
    JSON = "json"
    XML = "xml"


class CommandInterface(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs) -> str | None:
        pass


class DisplayInterface(ABC):
    @abstractmethod
    def display(self, book: Book, display_type: enum.Enum) -> None:
        pass


class PrinterInterface(ABC):
    @abstractmethod
    def print_book(self, book: Book, print_type: enum.Enum) -> None:
        pass


class SerializerInterface(ABC):
    @abstractmethod
    def serialize(self, book: Book, serialize_type: enum.Enum) -> str:
        pass
