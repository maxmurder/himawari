# himawari

Simple python script for getting the latest <a href="http://himawari8.nict.go.jp">Himawari 8</a> satellite images.

Also contains scripts to automate updating the desktop background using <a href="https://feh.finalrewind.org/">feh</a> image viewer.

### Usage:
`python3 himawari.py [-l --lod {4, 8, 16, 20}] [-f --format {png,jpg,bmp,tiff,pcx,ppm,im,eps,gif,spi,webp}] [-o --output <output.png>] [-r --retires <int>]`

-l --lod {4,8,16,20}      Image level of detail.

-f --format {png,jpg,bmp,tiff,pcx,ppm,im,eps,gif,spi,webp}      Output image format.

-o --output      Name of output file.

-r --retires      Number of times to retry connections before aborting. 


### Background Automation:
  ##### GNOME:
  1. Install scripts:
    `sudo cp himawari.py /usr/local/bin/ && sudo cp setBackground.sh /usr/local/bin/`
    `sudo chmod 755 /usr/local/bin/setBackground.sh`
  2. Create cron job to run the script:
    `*/10 * * * * /usr/local/bin/himawari/setBackground.sh`

 ##### feh:
  1. Install feh:
    `sudo apt-get install feh`
  2. Install scripts:
    `sudo cp himawari.py /usr/local/bin/ && sudo cp setBackground.sh /usr/local/bin/`
    `sudo chmod 755 /usr/local/bin/setBackgroundFeh.sh`
  3. Create cron job to run the script every:
    `*/10 * * * * /usr/local/bin/himawari/setBackground.sh`

 ##### MacOS:
  1. Install scripts:
    `sudo mkdir /opt/scripts/himawari`
    `sudo cp himawari.py /opt/scripts/himawari/ && sudo cp mac/updateBackgroundMac.sh /opt/scripts/himawari/ && sudo cp mac/setDesktops.applescript /opt/scripts/himawari/`
    `sudo chmod 755 /opt/scripts/himawari/setBackground.sh`
  2. Create launchd to run the scripts:
    `cp mac/com.himawariBackgorund.plist ~/Library/LaunchAgents/`
    `launchctl load ~/Library/LaunchAgents/com.himawariBackgorund.plist`
