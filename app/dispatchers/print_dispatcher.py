class PrintDispatcher:
    def __init__(
            self,
            allowed_printers: dict
    ) -> None:
        self.allowed_printers = allowed_printers

    def handle(self, method_type: str) -> None:
        if self.__is_print_type_valid(method_type):
            return self.allowed_printers[method_type].print()
        raise ValueError(f"Unknown print type: {method_type}")

    def __is_print_type_valid(self, method_type: str) -> bool:
        return method_type in self.allowed_printers
