import flags

class Bot():
    def __init__(self, family: bool):
        self.family = family

    def awake(self) -> None:
        print("I AM AWAKE")

    def sleep(self) -> None:
        flags.loop = flags.BotLoop.END
        print("I WILL SLEEP NOW")

