from app.models import Book


class BookPrinter:
    def print_book(self: Book, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {self.title}...")
            print(self.content)
        elif print_type == "reverse":
            print(f"Printing the book in reverse: {self.title}...")
            print(self.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {print_type}")


class BookView:
    def display(self: Book, display_type: str) -> None:
        if display_type == "console":
            print(self.content)
        elif display_type == "reverse":
            print(self.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {display_type}")
