#!/bin/bash

PID=$(id --real --user)
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/$PID/bus"

/usr/bin/python3 /usr/local/bin/rammb.py -q -s goes-18 -z 1 -d /tmp/ -f goes-18.png
/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:////tmp/goes-18.png

exit 0
