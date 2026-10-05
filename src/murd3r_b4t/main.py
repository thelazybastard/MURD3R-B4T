import argparse
import bot

def main() -> None:
    parser = argparse.ArgumentParser(
        prog="MURD3R-B4T", description="BOT SENT TO ANNIHILATE THE HUMAN RACE"
    )
    
    parser.add_argument(
        "-f",
        "--family",
        action=argparse.BooleanOptionalAction,
        help="Make the bot family friendly :)",
    )

    args = parser.parse_args()

    b4t = bot.Bot(args.family)

    while True:
        b4t.awake()

    b4t.sleep()


if __name__ == "__main__":
    main()
