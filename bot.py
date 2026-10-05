import re

class Bot():
    def __init__(self, formal: bool):
        self.formal = formal

    def awaken(self) -> None:
        if not self.formal:
            print("Yo, you good?")
        else:
            print("Good day, how are you?")

    def sleep(self) -> None:
        if not self.formal:
            print("See ya!")
        else:
            print("Have a great day! I hope we meet again")

    def converse(self, prompt: str) -> None:
        print(self.check_prompt(prompt))

    @staticmethod
    def check_prompt(prompt: str) -> str:
        pattern = r""
        match = re.findall(pattern, prompt, re.IGNORECASE)

        # placeholder replace later
        return match[0]

