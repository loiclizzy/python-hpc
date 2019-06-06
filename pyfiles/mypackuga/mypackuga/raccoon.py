"""Raccoon module
=================




"""

import argparse

doc = """Raccoon command line

Play with the raccoon...
"""


def main():
    print('in mypackuga.raccoon.main(): pouic pouic!')

    parser = argparse.ArgumentParser(
        description=doc,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument(
        'methods', nargs='?',
        help='Methods to use',
        type=str, default=None)

    parser.add_argument('-f', '--feature',
                        help='Use the feature ...',
                        action='store_false')

    args = parser.parse_args()
    print('args:', args)
