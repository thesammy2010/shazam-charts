import argparse
import logging
import re
import sys


# define cli argument parser
parser: argparse.ArgumentParser = argparse.ArgumentParser(
    prog="shazam",
    usage="shazam (chart|state_chart) <count>",
    epilog="",
    description="This tool gives us information on user data",
    add_help=False,
)

# add CLI arguments
parser.add_argument("type", type=str, help="Chart type")
parser.add_argument("count", type=int, help="The number of records returned ordered by highest to lowest")
parser.add_argument("-v", "--verbose", action="store_true", help="Set output verbosity")
parser.add_argument("-h", "--help", action="help", help="Display this message")


def main() -> None:
    """
    This is the main method used to interact with the CLI
    :return: None (nothing)
    """

    # parse arguments
    args, unknown = parser.parse_known_args()

    # handle verbosity
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")
    else:
        logging.basicConfig(level=logging.INFO, format="%(message)s")

    # notify if extra CLI arguments are passed
    if unknown:
        logging.warning(f"Unknown arguments {unknown} passed and are ignored")

    # check if count is valid
    if args.count <= 0:
        logging.error(f"Count {args.count} is invalid. Must be greater than 0")
        sys.exit(1)

    # check if chart type is valid
    if not re.search(r"(chart|state_chart)$", args.type):
        logging.error(f"Chart type {args.type} is invalid. Must be one of [chart, state_chart]")
        sys.exit(1)

    # exit as no other code has been implemented
    sys.exit(0)


if __name__ == "__main__":
    main()
