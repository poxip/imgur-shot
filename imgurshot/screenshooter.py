"""
Created on 25 Jan, 2015

Screenshoter module
"""

import os
import pyscreenshot as ImageGrab
import pyimgur

from time import time
from hashlib import sha1

class Screenshooter:
    def __init__(self, app_id):
        """Init the client with given imgur application id.
        :param app_id imgur application id
        """
        self.__imgur = pyimgur.Imgur(app_id)
        self.__save_dir = '{home}/.imgur-screenshooter'.format(
            home=os.environ['HOME']
        )
        # Ensure screenshots directory exists
        if not os.path.exists(self.__save_dir):
            os.makedirs(self.__save_dir)

    def grab(self):
        """Take a screenshot and saves it to $HOME/.imgur-screenshopter.

        :return path to the saved image.
        """
        image = ImageGrab.grab()
        filename_hash = sha1()
        filename_hash.update(str(time()))
        save_path = '{save_dir}/{hash}.jpg'.format(
            save_dir=self.__save_dir,
            hash=filename_hash.hexdigest()[:10]
        )
        image.save(save_path)

        return save_path

    def upload(self, image_path):
        """Upload a screenshot to imgur from given path.

        :param image_path A path to the image to be uploaded
        :return uploaded image data
        """
        return self.__imgur.upload_image(
            image_path, title="Uploaded with imgur-screenshooter"
        )
