# imgur-shot
_A simple screenshots tool written in Python, made for rapid screenshots sharing_

[![Build Status](https://travis-ci.org/poxip/imgur-shot.svg?branch=master)](https://travis-ci.org/poxip/imgur-shot)
[![PyPI Version](https://img.shields.io/pypi/v/imgur-shot.svg)](https://pypi.python.org/pypi/imgur-shot) 
[![PyPI License](https://img.shields.io/pypi/l/imgur-shot.svg)](https://github.com/poxip/imgur-shot/blob/master/LICENSE) 
[![PyPI Downloads](https://img.shields.io/pypi/dm/imgur-shot.svg)](https://pypi.python.org/pypi/imgur-shot)

__imgur-shot__ makes screeshots sharing much simpler! Just select the __whole display__, an __area__ or a __window__ (thanks to scrot), and wait for the link (libnotify included):
```
imgur-shot
```
or use the flag __--select__ to select a window or an area
```
imgur-shot --select
```
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
Make sure you have __all the dependencies__ (like _python-gobject_) installed.

Install the latest release using _pip_:
```
pip install imgur-shot
```
or get the latest source and execute:
```
./setup.py install
```
## Running
To take a screenshot __of the whole screen__ execute:
```
imgur-shot
```
use the flag __--select__ to select a window or an area
```
imgur-shot --select
```
Use __ESC__ to cancel.
## Setting up key bindings
As it's a screenshooting tool, you might want to set up some key bindings.
* __GNOME Shell__:

  The easiest way is to use _gnome-control-center_. If you don't know how to add a shortcut, please follow [this simple instruction](http://askubuntu.com/a/73488/281272).

  However you can set a shortcut thgrough the command line, but in this case you need to replace ___custom0___ and ___custom1___ with following suffix if you happen to have any other custom shortcuts set (e.g, _custom2_, _custom3_, etc). Also [this article from the Ubuntu Wiki](https://wiki.ubuntu.com/Keybindings) may come in handy.
  ```
  gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ name "imgur-shot"
  gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ command "imgur-shot"
  gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ binding "<Primary>1"

  gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/ name "imgur-shot select"
  gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/ command "imgur-shot --select"
  gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/ binding "<Primary>2"
  ```

After all you can press __CTRL+1__ to take a screenshot of the whole display and __CTRL+2__ for a window or an area.
  
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
