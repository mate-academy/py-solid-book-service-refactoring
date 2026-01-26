class CommandRegistry:
    def __init__(self):
        self._commands = {}

    def register(self, cmd_type, method_type, executor):
        self._commands[(cmd_type, method_type)] = executor

    def get_executor(self, cmd_type, method_type):
        return self._commands.get((cmd_type, method_type))

registry = CommandRegistry()