import argparse
import numpy as np
import matplotlib.colors as matplotlib_colors


def convert(start: str, end: str, quantity: int) -> list:
    if start[0] != "#":
        start = f"#{start}"
    if end[0] != "#":
        end = f"#{end}"
    colors = list(
        matplotlib_colors.LinearSegmentedColormap.from_list("", [start, end])(
            np.linspace(0, 1, quantity)
        )
    )
    hex_colors = [matplotlib_colors.to_hex(c) for c in colors]
    return hex_colors


parser = argparse.ArgumentParser(
    prog="coloripy",
    description="A small tool to generate monochromatic color palettes with Python.",
    epilog="Thanks for using coloripy!",
    usage="python main.py -s <start_color> -e <end_color> -q <quantity>",
)

parser.add_argument(
    "-s", "--start", help="The start color of the palette.", required=True
)

parser.add_argument("-e", "--end", help="The end color of the palette.", required=True)

parser.add_argument(
    "-q",
    "--quantity",
    help="The number of colors in the palette.",
    type=int,
    default=10,
)

args = parser.parse_args()

try:
    print(convert(args.start, args.end, args.quantity))
except Exception as e:
    print(f"An error occurred. ({e})")
