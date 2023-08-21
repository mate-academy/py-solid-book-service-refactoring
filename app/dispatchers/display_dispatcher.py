from app.displayers.displayers import (
    ConsoleDisplayer,
    ReverseDisplayer
)
from app.entities.book import Book


class DisplayDispatcher:
    ALLOWED_DISPLAYERS = {
        "console": ConsoleDisplayer,
        "reverse": ReverseDisplayer
    }

    def handle(self, method_type: str, book: Book) -> None:
        if self.__is_display_type_valid(method_type):
            return self.ALLOWED_DISPLAYERS[method_type](
                book
            ).display()
        raise ValueError(f"Unknown display type: {method_type}")

    def __is_display_type_valid(self, method_type: str) -> bool:
        return method_type in self.ALLOWED_DISPLAYERS
