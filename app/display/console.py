from app.display.base import BaseDisplayHandler


class ConsoleDisplayHandler(BaseDisplayHandler):
    def display(self, content: str) -> None:
        print(content)
