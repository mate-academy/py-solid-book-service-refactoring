class MethodValidator:
    def __init__(self, cmd_name: str, available_methods: [str]) -> None:
        self.cmd = cmd_name
        self.methods = available_methods

    def validate_method(self, method: str) -> None:
        if method not in self.methods:
            raise ValueError(f"Unknown {self.cmd} type: {method}")


class DisplayMethodValidator(MethodValidator):
    def __init__(self) -> None:
        super().__init__("display", ["console", "reverse"])


class SerializerMethodValidator(MethodValidator):
    def __init__(self) -> None:
        super().__init__("serialize", ["json", "xml"])


class PrinterMethodValidator(MethodValidator):
    def __init__(self) -> None:
        super().__init__("print", ["console", "reverse"])
