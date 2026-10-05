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
        print("FUCK YOU WANT?")

