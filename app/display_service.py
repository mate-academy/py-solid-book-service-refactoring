class DisplayService:
    @staticmethod
    def display(content, display_type):
        if display_type == "console":
            print(content)
        elif display_type == "reverse":
            print(content[::-1])
        else:
            raise ValueError(f"Unknown display type: {display_type}")
