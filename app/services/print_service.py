class PrintService:
    @staticmethod
    def print_book(title: str, content: str, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {title}...")
            print(content)
        elif print_type == "reverse":
            print(f"Printing the book in reverse: {title}...")
            print(content[::-1])
        else:
            raise ValueError(f"Unknown print type: {print_type}")
