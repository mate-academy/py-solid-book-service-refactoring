from app.interfaces import Printer


class ConsolePrinter(Printer):
    def print(self, title: str, content: str) -> None:
        print(content)


class ReverseConsolePrinter(Printer):
    def print(self, title: str, content: str) -> None:
        print(content[::-1])


class PrintConsolePrinter(Printer):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class PrintReverseConsolePrinter(Printer):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


class PrinterFactory:
    _display_printers = {
        "console": ConsolePrinter,
        "reverse": ReverseConsolePrinter,
    }
    _print_printers = {
        "console": PrintConsolePrinter,
        "reverse": PrintReverseConsolePrinter,
    }

    @staticmethod
    def create_display_printer(method_type: str) -> Printer:
        printer_class = PrinterFactory._display_printers.get(method_type)
        if printer_class is None:
            raise ValueError(f"Unknown display type: {method_type}")
        return printer_class()

    @staticmethod
    def create_print_printer(method_type: str) -> Printer:
        printer_class = PrinterFactory._print_printers.get(method_type)
        if printer_class is None:
            raise ValueError(f"Unknown print type: {method_type}")
        return printer_class()
