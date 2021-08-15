import argparse
import logging
import re
import sys
import typing

from shazam_charts.transform import transform


# define cli argument parser
parser: argparse.ArgumentParser = argparse.ArgumentParser(
    prog="shazam",
    usage="shazam (chart|state_chart) <count>",
    epilog="",
    description="This tool gives us information on user data",
    add_help=False,
)

# add CLI arguments
parser.add_argument("method", type=str, help="Chart type")
parser.add_argument("count", type=int, help="The number of records returned ordered by highest to lowest")
parser.add_argument("-v", "--verbose", action="store_true", help="Set output verbosity")
parser.add_argument("-h", "--help", action="help", help="Display this message")


def parse_args(args: typing.List[str]) -> (argparse.Namespace, typing.List[str]):
    """
    Method to parse string arguments
    :param args: List of arguments as a string
    :return: A tuple of (known arguments in a namespace, list of unparsed args)
    """
    return parser.parse_known_args(args)


def are_args_valid(args: argparse.Namespace, unknown: typing.List[str] = None) -> bool:
    """
    Determines if arguments are valid and returns a bool stating whether they are valid
    :param args: Namespace object of parsed arguments
    :param unknown: List of unparsed string arguments
    :return: True if the arguments are valid and false otherwise
    """
    # notify if extra CLI arguments are passed
    if unknown:
        logging.warning(f"Unknown arguments {unknown} passed and are ignored")
        return False

    # check if count is valid
    if args.count <= 0:
        logging.error(f"Count {args.count} is invalid. Must be greater than 0")
        return False

    # check if chart type is valid
    if not re.search(r"(chart|state_chart)$", args.method):
        logging.error(f"Chart type {args.method} is invalid. Must be one of [chart, state_chart]")
        return False

    return True


def main() -> None:
    """
    This is the main method used to interact with the CLI
    :return: None (nothing)
    """

    # parse arguments
    args, unknown = parse_args(sys.argv[1:])

    # handle verbosity
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")
    else:
        logging.basicConfig(level=logging.INFO, format="%(message)s")

    # validate args
    if not are_args_valid(args=args, unknown=unknown):
        sys.exit(1)

    # run main method
    transform(method=args.method, count=args.count)

    # exit gracefully
    sys.exit(0)


if __name__ == "__main__":
    main()
