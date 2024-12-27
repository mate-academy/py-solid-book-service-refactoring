from app.book import Book


def display(book: Book, display_type: str) -> None:
    if display_type == "console":
        print(book.content)
    elif display_type == "reverse":
        print(book.content[::-1])
    else:
        raise ValueError(f"Unknown display type: {display_type}")
