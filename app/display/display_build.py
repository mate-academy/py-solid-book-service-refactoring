from app.display.display_interface import (
    DisplayInterface,
    ConsoleDisplay,
    ReverseDisplay,
)


class DisplayBuild:
    @staticmethod
    def display_build(display_type: str) -> DisplayInterface:
        if display_type == "console":
            return ConsoleDisplay()
        elif display_type == "reverse":
            return ReverseDisplay()
        else:
            raise ValueError(f"Unknown display type: {display_type}")
