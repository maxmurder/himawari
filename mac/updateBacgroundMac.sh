#!/bin/bash

python3 /opt/scripts/himawari/himawari.py -o /tmp/himawariBG.png
osascript /opt/scripts/himawari/setDesktops.applescript
killall Dock