from app.cmd_manager.print.printers import (ConsolePrinter, Printer,
                                            ReversePrinter)
from app.validators import PrintTypeValidatorMixin


class PrintManager(PrintTypeValidatorMixin):
    def set_printer(self, print_type: str) -> Printer:
        self.validate_type(print_type)

        if print_type == "console":
            return ConsolePrinter()

        if print_type == "reverse":
            return ReversePrinter()
