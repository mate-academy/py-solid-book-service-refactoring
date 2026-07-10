from app.display.base import BaseDisplayHandler


class ReverseDisplayHandler(BaseDisplayHandler):
    def display(self, content: str) -> None:
        print(content[::-1])
