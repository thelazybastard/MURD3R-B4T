import argparse


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="MURD3R-B4T", description="BOT SENT TO ANNIHILATE THE HUMAN RACE"
    )
    parser.add_argument("prompt", type=str, help="What you want to say to the bot")
    parser.add_argument(
        "-f",
        "--family",
        action=argparse.BooleanOptionalAction,
        help="Make the bot family friendly :)",
    )

    args = parser.parse_args()

if __name__ == "__main__":
    main()
