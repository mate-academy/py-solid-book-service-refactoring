from app.interfaces import IWriter


class ConsoleWriter(IWriter):
    def write(self, text: str) -> None:
        print(text)


class FileWriter(IWriter):
    def __init__(self, filename: str):
        self.filename = filename

    def write(self, text: str) -> None:
        with open(self.filename, "a") as f:
            f.write(text + "\n")
