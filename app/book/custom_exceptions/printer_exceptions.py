class UnknownPrintTypeError(ValueError):
    def __init__(self, print_type: str) -> None:
        super().__init__(f"Unknown print type: {print_type}")
