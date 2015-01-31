#!/usr/bin/env python
'''
Created on 25 Jan, 2015

Main module of imgur-shot application.
'''

import imgurshot
import sys

def main():
    client = imgurshot.Screenshooter(CLIENT_ID)
    client.take()

CLIENT_ID = '424c87cf63c1515'
if __name__ == '__main__':
    sys.exit(main() or 0)