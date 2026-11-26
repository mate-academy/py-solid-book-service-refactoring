class DisplayTypeError(ValueError):
    def __init__(self, display_type: str) -> None:
        super().__init__(f"Unknown display type: {display_type}")


class PrintTypeError(ValueError):
    def __init__(self, print_type: str) -> None:
        super().__init__(f"Unknown print type: {print_type}")


class SerializeTypeError(ValueError):
    def __init__(self, serialize_type: str) -> None:
        super().__init__(f"Unknown serialize type: {serialize_type}")
