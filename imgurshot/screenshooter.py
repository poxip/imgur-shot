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
        if not Notify.init(imgurshot.__appname__):
            self.__show_message("error", "unable to initialize libnotify")

    def take(self, type='screen'):
        """Take a screenshot, upload it to imgur and
        show a notification about the results

        :param type Determines screenshot type, use 'select' to take
                    a screenshot of selected area/window (scrot --select)

        :return True if everything was successful, otherwise False
        """
        img_path = self._grab(type)
        if not img_path:
            return False

        uploaded_img = self._upload(img_path)

        self.__show_message(
            title="Uploaded",
            message=uploaded_img.link,
            message_type='notification',
            is_main=True,
            actions=[
                NotifyAction(
                    'copy-to-clipboard', "Copy", self.__on_notification_copytoclipboard
                )
            ]
        )

        return True

    def _grab(self, screenshot_type):
        """Take a screenshot and save it to $HOME/.imgur-screenshooter.

        :param type Determines screenshot type, use 'select' to take
                    a screenshot of selected area/window (scrot --select)
        :return path to the saved image or None if nothing was grabbed
        """
        self.__show_message("_grab", "taking a screenshot..")

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
            self.__show_message("__grab", "scrot error occurred")
            if result is 2:
                self.__show_message("_grab", "no area selected")

            return

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

    def __show_message(self, title, message="", message_type='debug',
                       icon='dialog-information', is_main=False, actions=[]):
        """Inform user about what's going on right now.

        :param title A message title
        :param message A message to show
        :param type Describes what type of message it is,
                    i.e., 'debug' or 'notification'
        :param icon The name of icon to be displayed in the notification
        :param is_main Determines if the app should be exited on notification's
                       closed callback
        :param actions A list of :class NotifyAction
                       containing all actions to be added to the notification.
                       :note type must be 'notification'
        """
        print("[imgur-shot]: {title}: {message}".format(**locals()))
        if message_type is not 'debug':
            notification = Notify.Notification.new(
                title, message, icon
            )
            for action in actions:
                notification.add_action(
                    action.name, action.text, action.callback
                )

            if is_main:
                notification.connect(
                    'closed', self.__on_mainnotification_closed
                )

            notification.show()
            # Wait for any action
            # what if user clicked on the link? -- the program will be still running
            # (no idea at the moment, how to avoid this)
            if actions:
                Gtk.main()

    # Callbacks
    def __on_mainnotification_closed(self, notification):
        """When the last notification is closed, quit."""
        if Notify.is_initted():
            Notify.uninit()

        Gtk.main_quit()

    def __on_notification_copytoclipboard(self, notification, action, user_data):
        clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        clipboard.set_text(notification.props.body, -1)
        self.__show_message(notification.props.body, "Copied to the clipboard")