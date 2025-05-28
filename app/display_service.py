from app.book_service import BookService


class DisplayService(BookService):
    def execute(self, method_type: str) -> None | str:
        if method_type == "console":
            print(self.book.content)
        elif method_type == "reverse":
            print(self.book.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {method_type}")
