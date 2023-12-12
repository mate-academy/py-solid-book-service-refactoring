class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class BookDisplay:
    @staticmethod
    def display(book: Book, display_type: str) -> None:
        if display_type == "console":
            print(book.content)
        elif display_type == "reverse":
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {display_type}")


class BookPrinter:
    @staticmethod
    def print_book(book: Book, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {book.title}...")
            print(book.content)
        elif print_type == "reverse":
            print(f"Printing the book in reverse: {book.title}...")
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {print_type}")
