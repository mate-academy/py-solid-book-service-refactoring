from app.book import Book, Info


class Display:
    @staticmethod
    def display(book: Book, display_type: str) -> None:
        if display_type == "console":
            Info.console(book)
        elif display_type == "reverse":
            Info.reverse(book)
        else:
            raise ValueError(f"Unknown display type: {display_type}")
