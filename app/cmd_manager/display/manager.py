from app.validators import DisplayTypeValidatorMixin
from app.cmd_manager.display.displayers import (
    Displayer, ConsoleDisplayer, ReverseDisplayer
)


class DisplayManager(DisplayTypeValidatorMixin):
    def set_displayer(self, display_type: str) -> Displayer:
        self.validate_type(display_type)

        if display_type == "console":
            return ConsoleDisplayer()

        if display_type == "reverse":
            return ReverseDisplayer()
