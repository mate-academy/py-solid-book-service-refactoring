from dataclasses import dataclass

from .display import DisplayService
from .printing import PrintService
from .serializers import SerializationService


@dataclass
class Book:
    title: str
    content: str

    def display(self, display_type: str) -> None:
        DisplayService.display(self, display_type)

    def print_book(self, print_type: str) -> None:
        PrintService.print_book(self, print_type)

    def serialize(self, serialize_type: str) -> str:
        return SerializationService.serialize(self, serialize_type)
