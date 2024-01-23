#!/usr/bin/env python3
"""
Author : ai-lien <ai-lien@localhost>
Date   : 2024-01-23
Purpose: Pack a picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Picnic game",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("items", metavar="str", nargs="+", help="Items to bring")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items

    if len(items) == 1:
        item_str = items[0]
    elif len(items) == 2:
        item_str = " and ".join(items)
    else:
        item_str = ", ".join(items[0:-1]) + ", and " + items[-1]

    print(f"You are bringing {item_str}.")


# --------------------------------------------------
if __name__ == "__main__":
    main()
