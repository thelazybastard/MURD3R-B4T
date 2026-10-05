import argparse
import bot

def main() -> None:
    parser = argparse.ArgumentParser(
        prog="roach", description="your best friend"
    )
    
    parser.add_argument(
        "-f",
        "--formal",
        action=argparse.BooleanOptionalAction,
        help="Make the bot more formal :)",
    )

    args = parser.parse_args()

    b4t = bot.Bot(args.formal)

    b4t.awaken()

    while True:
        prompt = input("Sentient: ")
        b4t.converse(prompt)

    b4t.sleep()


if __name__ == "__main__":
    main()
