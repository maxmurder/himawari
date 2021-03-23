# himawari

Simple python script for retrieving the latest <a href="http://himawari8.nict.go.jp">Himawari-8</a> and <a h ref="https://rammb-slider.cira.colostate.edu"/> GOES </a>satellite imagery and applying them as a updating desktop background.

Requires <a href="https://www.python.org/">Python 3</a> with the <a href="https://pypi.org/project/Pillow/">pillow</a> package. 

### Usage:
```
himawari.py [-l --lod {4, 8, 16, 20}] [-f --format {png,jpg,bmp,tiff,pcx,ppm,im,eps,gif,spi,webp}] 
	       [-o --output <output.png>] [-r --retires <int>]
-l --lod {4,8,16,20}      Image level of detail.
-f --format {png,jpg,bmp,tiff,pcx,ppm,im,eps,gif,spi,webp}      Output image format.
-o --output      Name of output file.
-r --retires      Number of times to retry connections before aborting.
```

#### RAAMB/CIRA:
For retrieving imagery from GOES, and a variety of other satilltes, including Himiwari-8, we use the <a href="https://rammb-slider.cira.colostate.edu"/>Colorado State University RAMMB/CIRA slider </a>api script: 
```
rammb.py [-h] [-s {goes-16,goes-17,himawari,meteosat-8,meteosat-11,jpss}] [-c SECTOR] [-p PRODUCT] [-z ZOOM]
                [-d DIRECTORY] [-f FILENAME] [-q]
optional arguments:
  -h, --help            show this help message and exit
  -s {goes-16,goes-17,himawari,meteosat-8,meteosat-11,jpss}, --sat {goes-16,goes-17,himawari,meteosat-8,meteosat-11,jpss}
                        satellite to retrieve data from.
  -c SECTOR, --sector SECTOR
                        image sector to retrieve.
  -p PRODUCT, --product PRODUCT
                        image product to retrieve.
  -z ZOOM, --zoom ZOOM  Zoom level to use. 0-4
  -d DIRECTORY, --directory DIRECTORY
                        output directory for image.
  -f FILENAME, --filename FILENAME
                        filename for output
```


### Background Automation:
  ##### Linux:
  1. Install scripts (to a location of your choice):

    sudo cp himawari.py /usr/local/bin/ && sudo cp rammb.py /usr/local/bin/ && sudo cp set-background.sh /usr/local/bin/
    sudo chmod 755 /usr/local/bin/set-background.sh
  2. Create cron job to run the script (satellites update every 10 mins).

	crontab -e
  4. Add this line:
 
  	*/10 * * * * /usr/local/bin/set-background.sh
  ##### Windows:
  1. Add an task in the windows task scheduler to run update-backgound.bat on a repeating interval:
  
  	update-backgound.bat C:\User\Urist\Pictures\Backgounds
  2. Set the desktop backgound mode to slideshow, and select one of the output directories as the source.
    
    
