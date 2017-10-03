#!/bin/bash

/usr/bin/python3 /usr/local/bin/himawari.py -o /tmp/himawariBG.png
/usr/bin/gconftool-2 --type string --set /desktop/gnome/background/picture_filename /tmp/himawariBG.png
exit 0
