user_response: dict[str, list[str]] = {
    "USER_HAPPY": ["good", "great", "swell", "jolly", "delightful"],

    "USER_NEUTRAL": ["fine", "ok", "decent", "well", "enough"],

    "USER_SAD": ["bad", "sad", "tired", "unhappy", "need", "talk"],

    "USER_FRUSTRATED": ["crap", "horrible", "hate", "frustrated"],

    "USER_ANGRY": ["fuck", "bitch", "evil", "hate", "cunt", "asshole"],
}

bot_response: dict[str, list[str]] = {
    "curious": [
        "Tell me more!",
        "I'd love to hear more about it",
        "I want to know more, if that's ok",
    ],

    "ponder": [
        "I wonder why that is?",
        "It is strange, why is that?",
        "How does that work, I wonder?"
    ],

    "advice": [
        "You know, a great philosopher once said 'Happiness depends upon ourselves'",
        "I am always here if you need to speak to me.",
        "You should reach out to those closest to you!"
    ],

    "calm": [
        "I understand you are angry. Let's all take a deep breath!",
        "We all feel that way, please don't feel ashamed of it",
        "Let's talk about what's bothering you. Maybe I can help?"
    ]
}