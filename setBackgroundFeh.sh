#!/bin/bash

export DISPLAY=':0'
export XAUTHORITY='$HOME/.Xauthority'

/usr/bin/python3 /usr/local/bin/himawari.py -o /tmp/himawariBG.png
/usr/bin/feh --bg-max /tmp/himawariBG.png
/bin/chmod 666 /tmp/himawariBG.png
exit 0
