"""
Created on 25 Jan, 2015

Screenshoter module
"""

import os
import subprocess
import pyimgur
import imgurshot

from time import time
from hashlib import sha1
from gi.repository import Notify
from gi.repository import Gtk, Gdk

class NotifyAction:
    """An notify action data carrier"""
    def __init__(self, name, text, callback):
        """Init the Action field with specified action name, text and callback.

        :param name Action's name used to identify the action
        :param text A text to be displayed
        :param callback A callback called when action was triggered
        """
        self.name = name
        self.text = text
        self.callback = callback

class Screenshooter:
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

        # Initialize libnotify
        Gtk.init()
        Notify.init(imgurshot.__appname__)

    def take(self):
        """Take a screenshot, upload it to imgur and
        show a notification about the results"""
        img_path = self._grab()
        uploaded_img = self._upload(img_path)

        self.__show_message(
            "Uploaded", uploaded_img.link, 'notification',
            actions=[NotifyAction(
                'copy-to-clipboard', "Copy", self.__on_notify_copytoclipboard
            )]
        )

    def _grab(self):
        """Take a screenshot and save it to $HOME/.imgur-screenshooter.

        :return path to the saved image
        """
        self.__show_message("Taking a screenshot..")

        filename_hash = sha1()
        filename_hash.update(str(time()).encode('utf-8'))
        save_path = '{save_dir}/{hash}.png'.format(
            save_dir=self.__save_dir,
            hash=filename_hash.hexdigest()[:10]
        )

        # Take a screenshot
        # TODO: Provide more control: selecting the area, window, etc (e.g, scrot -s)
        subprocess.call(['scrot', save_path])

        return save_path

    def _upload(self, image_path):
        """Upload a screenshot to imgur from given path.

        :param image_path A path to the image to be uploaded
        :return uploaded image data
        """
        self.__show_message("Uploading..", "", 'notification')
        return self.__imgur.upload_image(
            image_path, title="Uploaded with imgur-shot tool"
        )

    def __show_message(self, title, message="", type='debug',
                       icon='dialog-information', actions=[]):
        """Inform user about what's going on right now.

        :param title A message title
        :param message A message to show
        :param type Describes what type of message it is,
                    i.e., 'debug' or 'notification'
        :param icon The name of icon to be displayed in the notification
        :param actions A list of :class NotifyAction
                       containing all actions to be added to the notification.
                       :note type must be 'notification'
        """
        print("imgur-shot: {title} {message}".format(**locals()))
        if type is not 'debug':
            notification = Notify.Notification.new(
                title, message, icon
            )
            for action in actions:
                notification.add_action(
                    action.name, action.text, action.callback
                )

            notification.show()
            # An ugly hack to make actions working
            if actions:
                Gtk.main()

    # Callbacks
    def __on_notify_copytoclipboard(self, notification, action, user_data):
        clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        clipboard.set_text(notification.props.body, -1)
        self.__show_message(notification.props.body, "Copied to the clipboard")

        Gtk.main_quit()