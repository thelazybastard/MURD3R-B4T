import dialogue
from enum import Enum, auto
import random

class UserState(Enum):
    USER_HAPPY = auto()
    
    USER_NEUTRAL = auto()
    
    USER_SAD = auto()
    
    USER_FRUSTRATED = auto()
    
    USER_ANGRY = auto()

class Bot():
    def __init__(self, formal: bool):
        self.formal: bool = formal
        self.user_state: UserState = UserState.USER_NEUTRAL

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
        self.user_state = UserState[self.check_prompt(prompt)]

        match self.user_state:
            case UserState.USER_HAPPY: print(self.format_response(dialogue.bot_response[self.user_state.name]))
            case UserState.USER_NEUTRAL: print(dialogue.bot_response[self.user_state.name])
            case UserState.USER_SAD: print(dialogue.bot_response[self.user_state.name])
            case UserState.USER_FRUSTRATED: print(dialogue.bot_response[self.user_state.name])
            case UserState.USER_ANGRY: print(dialogue.bot_response[self.user_state.name])

    @staticmethod
    def check_prompt(prompt: str) -> str:
        words = prompt.split(" ")
        for word in words:
            for emotion, expected_words in dialogue.user_response.items():
                if word in expected_words:
                    return emotion

        return UserState.USER_NEUTRAL.name

    @staticmethod
    def format_response(response: list[str]) -> str:
        return random.choice(response) 