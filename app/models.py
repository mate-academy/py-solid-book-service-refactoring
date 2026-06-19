from dataclasses import dataclass


@dataclass
class Book:
    title: str
    content: str

    def display(self, display_type: str) -> None:
        from app.services import display_book

        display_book(self, display_type)

    def print_book(self, print_type: str) -> None:
        from app.services import print_book

        print_book(self, print_type)

    def serialize(self, serialize_type: str) -> str:
        from app.services import serialize_book

        return serialize_book(self, serialize_type)
