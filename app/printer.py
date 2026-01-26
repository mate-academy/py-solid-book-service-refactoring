class Printer:
    def __init__(self, book):
        self.book = book

    def print_console(self):
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)

    def print_reverse(self):
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])

    def print_content(self, method_type: str):
        method_name = f"print_{method_type}"
        method = getattr(self, method_name, None)

        if not callable(method):
            raise ValueError(f"Unknown print type: {method_type}")

        method()
