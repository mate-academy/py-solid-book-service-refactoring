from app.models import Book


def console_display(book: Book) -> None:
    print(book.content)


def reverse_display(book: Book) -> None:
    print(book.content[::-1])


def console_print(book: Book) -> None:
    print(f"Printing the book: {book.title}...")
    print(book.content)


def reverse_print(book: Book) -> None:
    print(f"Printing the book in reverse: {book.title}...")
    print(book.content[::-1])


DISPLAYERS = {"console": console_display, "reverse": reverse_display}
PRINTERS = {"console": console_print, "reverse": reverse_print}


def print_book(book: Book, print_type: str) -> None:
    if print_type in PRINTERS:
        PRINTERS[print_type](book)
    else:
        raise ValueError(f"Unknown print type: {print_type}")


def display(book: Book, display_type: str) -> None:
    if display_type in DISPLAYERS:
        DISPLAYERS[display_type](book)
    else:
        raise ValueError(f"Unknown display type: {display_type}")
