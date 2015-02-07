#!/usr/bin/env python
"""
Main module of imgur-shot application.
"""

import sys
import argparse

from imgurshot import __description__
from imgurshot.guiclient import GuiClient

def main():
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument(
        '--select',
        action='store_true',
        help="interactively choose a window or rectangle with the mouse"
    )
    args = parser.parse_args()

    client = GuiClient(CLIENT_ID)
    client.take('select' if args.select else 'screen')

CLIENT_ID = '424c87cf63c1515'
if __name__ == '__main__':
    sys.exit(main() or 0)