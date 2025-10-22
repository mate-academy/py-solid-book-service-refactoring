from app.interfaces.book_printer_interface import BookPrinterInterface


class ConsoleBookPrinter(BookPrinterInterface):
    @staticmethod
    def print_book(book: "Book") -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReverseBookPrinter(BookPrinterInterface):
    @staticmethod    
    def print_book(book: "Book") -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
