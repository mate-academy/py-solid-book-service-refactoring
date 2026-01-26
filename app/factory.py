from app.interface import (
    IDisplayProcessor,
    ConsoleDisplayProcessor,
    ReverseDisplayProcessor,
    ConsolePrintProcessor,
    IPrintProcessor,
    ReversePrintProcessor,
    ISerializeProcessor,
    JsonSerializeProcessor,
    XmlSerializeProcessor
)


class DisplayFactory:
    @staticmethod
    def get(display_type: str) -> IDisplayProcessor:
        match display_type:
            case "console":
                return ConsoleDisplayProcessor()
            case "reverse":
                return ReverseDisplayProcessor()
            case _:
                raise ValueError(f"Unknown display type: {display_type}")


class PrintFactory:
    @staticmethod
    def get(display_type: str) -> IPrintProcessor:
        match display_type:
            case "console":
                return ConsolePrintProcessor()
            case "reverse":
                return ReversePrintProcessor()
            case _:
                raise ValueError(f"Unknown print type: {display_type}")


class SerializeFactory:
    @staticmethod
    def get(serialize_type: str) -> ISerializeProcessor:
        match serialize_type:
            case "json":
                return JsonSerializeProcessor()
            case "xml":
                return XmlSerializeProcessor()
            case _:
                raise ValueError(f"Unknown serialize type: {serialize_type}")
