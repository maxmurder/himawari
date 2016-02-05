#!/bin/bash

# export DBUS_SESSION_BUS_ADDRESS environment variable
PID=$(pgrep gnome-session)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

python3 himawari.py -o /tmp/himawariBG.png
gsettings set org.gnome.desktop.background picture-uri file:///tmp/himawariBG.png
gsettings set org.gnome.desktop.background picture-options scaled
