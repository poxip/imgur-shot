#!/usr/bin/env python
"""
Main module of imgur-shot application.
"""

import sys
import argparse
import imgurshot

def main():
    parser = argparse.ArgumentParser(description=imgurshot.__description__)
    parser.add_argument(
        '--select',
        action='store_true',
        help="interactively choose a window or rectangle with the mouse"
    )
    args = parser.parse_args()

    client = imgurshot.Screenshooter(CLIENT_ID)
    client.take('select' if args.select else 'screen')

CLIENT_ID = '424c87cf63c1515'
if __name__ == '__main__':
    sys.exit(main() or 0)