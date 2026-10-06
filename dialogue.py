user_response: dict[str, list[str]] = {
    "USER_HAPPY": ["good", "great", "swell", "jolly", "delightful"],

    "USER_NEUTRAL": ["fine", "ok", "decent", "well", "enough"],

    "USER_SAD": ["bad", "sad", "tired", "unhappy", "need", "talk"],

    "USER_FRUSTRATED": ["crap", "horrible", "hate", "frustrated"],

    "USER_ANGRY": ["fuck", "bitch", "evil", "hate", "cunt", "asshole"],

    "EXIT": ["go now", "bye", "good day", "screw this", "leave me alone"]
}

bot_response: dict[str, list[str]] = {
    "USER_HAPPY": [
        "Tell me more!",
        "I'd love to hear more about it",
        "I want to know more, if that's ok",
    ],

    "USER_NEUTRAL": [
        "You know, a great philosopher once said 'Happiness depends upon ourselves'",
        "I am always here if you need to speak to me.",
        "You should reach out to those closest to you!"
    ],

    "USER_SAD": [
        "I wonder why that is?",
        "It is strange, why is that?",
        "How does that work, I wonder?"
    ],

    "USER_FRUSTRATED": [
        "I understand you are frustrated. Let's all take a deep breath!",
        "We all feel that way, please don't feel ashamed of it",
        "Let's talk about what's bothering you. Maybe I can help?"
    ],

    "USER_ANGRY": [
        "I understand you are angry. Let's all take a deep breath!",
        "We all feel that way, please don't feel ashamed of it",
        "Hey, i understand you're pissed, I would be too, but we need to stay calm"
    ],

    "EXIT": [
        "Very well",
        "Then i'll see you next time",
        "I won't keep you further"
    ]
}