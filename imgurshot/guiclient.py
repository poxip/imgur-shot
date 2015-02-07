"""
The Gui client module
"""

from imgurshot import __appname__
from imgurshot.client import Client

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

class GuiClient(Client):
    """The GUI Client implementing all GUI features, e.g. notifications."""

    def __init__(self, app_id):
        """Init the client with given imgur application id.

        :param app_id imgur application id
        """
        Client.__init__(self, app_id)

        # Initialize libnotify
        Gtk.init()
        if not Notify.init(__appname__):
            self._show_message("error", "unable to initialize libnotify")

    def take(self, type='screen'):
        """Take a screenshot, upload it to imgur and
        show a notification about the results

        :param type Determines screenshot type, use 'select' to take
                    a screenshot of selected area/window (scrot --select)

        :return url to the saved image if everything went successful,
                otherwise None
        """
        img_url = Client.take(self, type)
        if not img_url:
            return

        self._show_message(
            title="Uploaded",
            message=img_url,
            message_type='notification',
            is_main=True,
            actions=[
                NotifyAction(
                    'copy-to-clipboard', "Copy",
                    self.__on_notification_copytoclipboard
                )
            ]
        )

        return img_url

    def _show_message(self, title, message="", message_type='debug',
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
        if message_type is 'notification':
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
            # what if user clicked on the link?
            # -- the program will be still running
            # (no idea at the moment, how to avoid this)
            if actions:
                Gtk.main()

        else:
            Client._show_message(self, title, message)

    # Callbacks
    def __on_mainnotification_closed(self, notification):
        """When the last notification is closed, quit."""
        if Notify.is_initted():
            Notify.uninit()

        Gtk.main_quit()

    def __on_notification_copytoclipboard(self, notification, *args):
        clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        clipboard.set_text(notification.props.body, -1)
        Client._show_message(
            self, notification.props.body, "Copied to the clipboard"
        )