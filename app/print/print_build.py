from app.print.print_interface import (
    PrintBookInterface,
    ConsolePrint,
    ReversePrint
)


class PrintBuild:
    @staticmethod
    def print_build(print_type: str) -> PrintBookInterface:
        if print_type == "console":
            return ConsolePrint()
        elif print_type == "reverse":
            return ReversePrint()
        else:
            raise ValueError(f"Unknown print type: {print_type}")
