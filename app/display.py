class ConsoleDisplay:
    def display(self, book):
        print(book.content)


class ReverseDisplay:
    def display(self, book):
        print(book.content[::-1])
