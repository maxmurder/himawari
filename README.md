# himawari

Simple python script for getting the latest himawari satellite images.

Also contains scripts to update the desktop background to the latest image.

Usage:
python3 himawari.py [-l --lod {4, 8, 16, 20}] [-f --format {png,jpg,bmp,tiff,pcx,ppm,im,eps,gif,spi,webp}] [-o --output <output.png>] [-r --retires <int>]

-l --lod {4,8,16,20}      Image level of detail.

-f --format {png,jpg,bmp,tiff,pcx,ppm,im,eps,gif,spi,webp}      Output image format.

-o --output      Name of output file.

-r --retires      Number of times to retry connections before aborting. 


Background Automation:
  GNOME:
  1. Install scripts:
    `sudo mkdir /opt/scripts/himawari`
    `sudo cp himawari.py /opt/scripts/himawari/ && sudo cp setBackground.sh /opt/scripts/himawari/`
    `sudo chmod 755 /opt/scripts/himawari/setBackground.sh`
  2. Create cron job to run the script every 10 miniutes:
    `*/10 * * * * /opt/scripts/himawari/setBackground.sh`

  MacOS:
  1. Install scripts:
    `sudo mkdir /opt/scripts/himawari`
    `sudo cp himawari.py /opt/scripts/himawari/ && sudo cp mac/updateBackgroundMac.sh /opt/scripts/himawari/ && sudo cp mac/setDesktops.applescript /opt/scripts/himawari/`
    `sudo chmod 755 /opt/scripts/himawari/setBackground.sh`
  2. Create launchd to run the scripts:
    `cp mac/com.himawariBackgorund.plist ~/Library/LaunchAgents/`
    `launchctl load ~/Library/LaunchAgents/com.himawariBackgorund.plist`
