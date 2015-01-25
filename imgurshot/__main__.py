#!/usr/bin/env python2
'''
Created on 25 Jan, 2015

Main module of imgur-shot application.
'''

import imgurshot
import sys

# Currently this only works with Python2
# TODO: move from pyscreenshot and use Python3

def main():
    client = imgurshot.Screenshooter(CLIENT_ID)
    img_path = client.grab()
    uploaded_img = client.upload(img_path)
    print(uploaded_img.link)

CLIENT_ID = '424c87cf63c1515'
if __name__ == '__main__':
    sys.exit(main() or 0)