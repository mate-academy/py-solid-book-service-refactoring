from app.book import Book


class Print(Book):

    def do_action(self):
        raise NotImplementedError("Must override this method")


class PrintConsole(Print):

    def do_action(self) -> None:
        print(f"Printing the book: {self.title}...")
        self.print_content()


class PrintReverse(Print):

    def do_action(self):
        print(f"Printing the book in reverse: {self.title}...")
        self.print_content_reverse()
