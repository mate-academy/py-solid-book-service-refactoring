from abc import ABC, abstractmethod

AVAILABLE_COMMANDS = ("print", "display", "serialize",)

AVAILABLE_PRINT_TYPES = ("console", "reverse",)
AVAILABLE_DISPLAY_TYPES = ("console", "reverse",)
AVAILABLE_SERIALIZE_TYPES = ("json", "xml",)


class CommandValidatorMixin:
    @staticmethod
    def validate_command(command: str) -> None:
        if command not in AVAILABLE_COMMANDS:
            raise ValueError(f"Unknown command: {command}. "
                             "Choose correct command from the list: "
                             f"{AVAILABLE_COMMANDS}")


class TypeValidator(ABC):
    @staticmethod
    @abstractmethod
    def validate_type(method_type: str) -> None:
        pass


class PrintTypeValidatorMixin(TypeValidator):
    @staticmethod
    def validate_type(method_type: str) -> None:
        if method_type not in AVAILABLE_PRINT_TYPES:
            raise ValueError(f"Unknown print type: {method_type}")


class DisplayTypeValidatorMixin(TypeValidator):
    @staticmethod
    def validate_type(method_type: str) -> None:
        if method_type not in AVAILABLE_DISPLAY_TYPES:
            raise ValueError(f"Unknown display type: {method_type}")


class SerializeTypeValidatorMixin(TypeValidator):
    @staticmethod
    def validate_type(method_type: str) -> None:
        if method_type not in AVAILABLE_SERIALIZE_TYPES:
            raise ValueError(f"Unknown serialize type: {method_type}")
