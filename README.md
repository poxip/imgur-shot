# imgur-shot [![Build Status](https://travis-ci.org/poxip/imgur-shot.svg?branch=master)](https://travis-ci.org/poxip/imgur-shot)
A simple app made for rapid screenshots sharing.

__imgur-shot__ takes a screenshot using scrot and __uploads__ it to imgur.
## Requirements
* scrot
* libnotify-dev
* libgtk-3-dev
* python-gobject

### Debian Quickstart
```
apt-get install scrot libnotify-dev libgtk-3-dev python-gobject
```
## Installation
```
./setup.py install
```
## Running
To take a screenshot __of whole screen__ execute:
```
imgur-shot
```
use flag __--select__ to select a window or an area
```
imgur-shot --select
```
Use __ESC__ to cancel.
## Setting key bindings
As it's a screenshooting tool, you might want to set up some key bindings.
* __GNOME Shell__:

  The easiest way is to use _gnome-control-center_. If you don't know how to add it, please follow [this simple instruction](http://askubuntu.com/a/73488/281272).

  However you can do it using command line, but you will need to replace ___custom0___ and ___custom1___ with following suffix if you have any other custom shortcuts set (e.g, _custom2_, _custom3_, etc), also [this article from Ubuntu Wiki](https://wiki.ubuntu.com/Keybindings) might be useful.
  ```
  gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ name "imgur-shot"
  gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ command "imgur-shot"
  gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ binding "<Primary>1"

  gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/ name "imgur-shot select"
  gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/ command "imgur-shot --select"
  gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/ binding "<Primary>2"
  ```

And then just use __CTRL+1__ to take a screenshot of whole display and __CTRL+2__ to select the area.
  
## License
The MIT License (MIT)

Copyright (c) 2015 Michal Proszek

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
