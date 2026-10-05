import re

class Bot():
    def __init__(self, family: bool):
        self.family = family

    def awaken(self) -> None:
        if not self.family:
            print("Fuck off!")
        else:
            print("Leave me alone!")

    def sleep(self) -> None:
        if not self.family:
            print("Good fucking riddance!")
        else:
            print("Finally!")

    def converse(self, prompt: str) -> None:
        if not self.family:
            print("FUCK YOU WANT?")
        else:
            print("Ya got something to say?")

    @staticmethod
    def check_prompt(prompt: str) -> str:
        pattern = r""
        match = re.findall(pattern, prompt, re.IGNORECASE)

        # placeholder replace later
        return match[0]

