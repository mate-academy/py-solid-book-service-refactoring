from app.display import Display
from app.print import Print
from app.serializers import Serializer


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def apply_display_strategy(self, display_strategy: Display) -> None:
        display_strategy.display(self.content)

    def apply_print_strategy(self, print_strategy: Print) -> None:
        print_strategy.print_book(self.title, self.content)

    def apply_serialization_strategy(
            self,
            serialization_strategy: Serializer
    ) -> str:
        return serialization_strategy.serialize(self.title, self.content)
