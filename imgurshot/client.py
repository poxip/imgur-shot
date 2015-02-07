"""
Screenshooter module
"""

import os
import subprocess
import pyimgur

from time import time
from hashlib import sha1

class Client:
    """Base client for imgur-shot"""

    def __init__(self, app_id):
        """Init the client with given imgur application id.

        :param app_id imgur application id
        """
        self.__imgur = pyimgur.Imgur(app_id)
        self.__save_dir = '{home}/.imgur-screenshooter'.format(
            home=os.environ['HOME']
        )
        # Ensure that the screenshots' directory exists
        if not os.path.exists(self.__save_dir):
            os.makedirs(self.__save_dir)

    def take(self, type='screen'):
        """Take a screenshot, upload it to imgur and
        inform about the results.

        :param type Determines screenshot type, use 'select' to take
                    a screenshot of selected area/window (scrot --select)

        :return url to the saved image if everything went successful,
                otherwise None
        """
        img_path = self._grab(type)
        if not img_path:
            return

        uploaded_img = self._upload(img_path)
        self._show_message(
            title="Uploaded",
            message=uploaded_img.link
        )

        return uploaded_img.link

    def _grab(self, screenshot_type):
        """Take a screenshot and save it to $HOME/.imgur-screenshooter.

        :param type Determines screenshot type, use 'select' to take
                    a screenshot of selected area/window (scrot --select)
        :return path to the saved image or None if nothing was grabbed
        """
        self._show_message("_grab", "taking a screenshot..")

        filename_hash = sha1()
        filename_hash.update(str(time()).encode('utf-8'))
        save_path = '{save_dir}/{hash}.png'.format(
            save_dir=self.__save_dir,
            hash=filename_hash.hexdigest()[:10]
        )

        # Take a screenshot
        screenshot_select = [
            '--select', '--border'
        ] if screenshot_type is 'select' else []

        scrot_command = ['scrot', save_path]
        if screenshot_select:
            scrot_command += screenshot_select

        result = subprocess.call(scrot_command)
        if result is not 0:
            self._show_message("__grab", "scrot error occurred")
            if result is 2:
                self._show_message("_grab", "no area selected")

            return

        return save_path

    def _upload(self, image_path):
        """Upload a screenshot to imgur from given path.

        :param image_path A path to the image to be uploaded
        :return uploaded image data
        """
        self._show_message("Uploading..", "")
        return self.__imgur.upload_image(
            image_path, title="Uploaded with imgur-shot tool"
        )

    def _show_message(self, title, message=""):
        """Inform user about what's going on right now.

        By default messages are logged to stdout.

        :param title A message title
        :param message A message to show
        """
        print("[imgur-shot]: {title}: {message}".format(
            title=title,
            message=message
        ))
