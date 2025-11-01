from app.models import Book


class BaseDisplayStrategy:
    def display(self, book: Book) -> None:
        raise NotImplementedError


class ConsoleDisplay(BaseDisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(BaseDisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class BookDisplay:
    _strategies = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }

    @staticmethod
    def display(book: Book, display_type: str) -> None:
        strategy = BookDisplay._strategies.get(display_type)
        if not strategy:
            raise ValueError(f"Unknown display type: {display_type}")
        strategy.display(book)
