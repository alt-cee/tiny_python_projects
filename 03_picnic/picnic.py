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
    pos_arg = args.items

    print(f'positional = "{pos_arg}"')


# --------------------------------------------------
if __name__ == "__main__":
    main()
