from app.book_service import BookService


class PrintService(BookService):
    def execute(self, method_type: str) -> None | str:
        if method_type == "console":
            print(f"Printing the book: {self.book.title}...")
            print(self.book.content)
        elif method_type == "reverse":
            print(f"Printing the book in reverse: {self.book.title}...")
            print(self.book.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {method_type}")
