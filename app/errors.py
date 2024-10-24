class UnknownCommandError(Exception):
    def __init__(self, command: str) -> None:
        super().__init__(f"Unknown command: {command}")


class UnknownTypeError(Exception):
    def __init__(self, command: str, method_type: str) -> None:
        super().__init__(f"Unknown {command} type: {method_type}")


class UnknownDisplayTypeError(UnknownTypeError):
    pass


class UnknownPrintTypeError(UnknownTypeError):
    pass


class UnknownSerializerTypeError(UnknownTypeError):
    pass
