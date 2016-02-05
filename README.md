# himawari

Simple python script for getting the latest himawari sattilite images.

usage: himawari.py [-h] [-l {4,8,16,20}]
                   [-f {png,jpg,bmp,tiff,pcx,ppm,im,eps,gif,spi,webp}]
                   [-o OUT] [-r RETRIES]

optional arguments:
  -h, --help            show this help message and exit
  -l {4,8,16,20}, --lod {4,8,16,20}
                        Set level of detail for image. Valid values: 4, 8, 16,
                        20
  -f {png,jpg,bmp,tiff,pcx,ppm,im,eps,gif,spi,webp}, --format {png,jpg,bmp,tiff,pcx,ppm,im,eps,gif,spi,webp}
                        Output format.
  -o OUT, --out OUT     Name of output file.
  -r RETRIES, --retries RETRIES
                        Number of retrys for http failures

