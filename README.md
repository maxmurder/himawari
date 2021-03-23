# himawari

Simple python script for retrieving the latest <a href="http://himawari8.nict.go.jp">Himawari 8</a> and <https://rammb-slider.cira.colostate.edu/> GOES </a>satellite imagery and applying them as a updating desktop background.


### Usage:
`python3 himawari.py [-l --lod {4, 8, 16, 20}] [-f --format {png,jpg,bmp,tiff,pcx,ppm,im,eps,gif,spi,webp}] [-o --output <output.png>] [-r --retires <int>]`
-l --lod {4,8,16,20}      Image level of detail.
-f --format {png,jpg,bmp,tiff,pcx,ppm,im,eps,gif,spi,webp}      Output image format.
-o --output      Name of output file.
-r --retires      Number of times to retry connections before aborting. 


rammb.py [-h] [-s {goes-16,goes-17,himawari,meteosat-8,meteosat-11,jpss}] [-c SECTOR] [-p PRODUCT] [-z ZOOM]
                [-d DIRECTORY] [-f FILENAME] [-q]

optional arguments:
  -h, --help            show this help message and exit
  -s {goes-16,goes-17,himawari,meteosat-8,meteosat-11,jpss}, --sat {goes-16,goes-17,himawari,meteosat-8,meteosat-11,jpss}
                        Satellite to get data for.
  -c SECTOR, --sector SECTOR
                        Image sector to retrieve.
  -p PRODUCT, --product PRODUCT
                        Image product to retrieve.
  -z ZOOM, --zoom ZOOM  Zoom level to use. 0-4
  -d DIRECTORY, --directory DIRECTORY
                        Output directory for image.
  -f FILENAME, --filename FILENAME
                        Filename for output



### Background Automation:
  ##### GNOME:
  1. Install scripts:
    `sudo cp himawari.py /usr/local/bin/ && sudo cp setBackground.sh /usr/local/bin/`
    `sudo chmod 755 /usr/local/bin/set-background.sh`
  2. Create cron job to run the script (satellites update every 10 mins).
	`crontab -e`
	a. Add this line:
    `*/10 * * * * /usr/local/bin/himawari/setBackground.sh`