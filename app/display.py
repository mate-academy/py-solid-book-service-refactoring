from app.book import Book


class Display(Book):

    def do_action(self):
        raise NotImplementedError("Must override this method")


class DisplayConsole(Display):
    def do_action(self) -> None:
        self.print_content()


class DisplayReverse(Display):
    def do_action(self) -> None:
        self.print_content_reverse()
