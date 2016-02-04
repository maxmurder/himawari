#!/usr/bin/env python3

from io import BytesIO
from json import loads
from time import strptime, strftime
from PIL import Image
from urllib.request import urlopen
import argparse

def main():

	level = 4
	height = 550
	width = 550
	outfile = ''

	parser = argparse.ArgumentParser()
	parser.add_argument("-l", "--lod", choices=[4,8,16,20], help="Set level of detail for image. Valid values: 4, 8, 16, 20", type=int)
	parser.add_argument("-o", "--out", help="Name of output file.")

	args = parser.parse_args()
	if args.lod == 8:
		level = 8
	elif args.lod == 16:
		level = 16
	elif args.lod ==20:
		level = 20

	if args.out is not None:
		outfile = args.out


	with urlopen("http://himawari8-dl.nict.go.jp/himawari8/img/D531106/latest.json") as latest_json:	
		latest = strptime(loads(latest_json.read().decode("utf-8"))["date"], "%Y-%m-%d %H:%M:%S")

	print("Latest: {} GMT\n".format(strftime("%Y/%m/%d/%H:%M:%S",latest)))

	url_format = "http://himawari8.nict.go.jp/img/D531106/{}d/{}/{}_{}_{}.png"

	img = Image.new('RGB',(width*level, height*level))

	print("Downloading: 0/{}".format(level*level), end="\r")

	for x in range(level):
		for y in range(level):
			with urlopen(url_format.format(level,width,strftime("%Y/%m/%d/%H%M%S",latest), x, y)) as tile_w:
				tileData = tile_w.read()

			tile = Image.open(BytesIO(tileData))

			img.paste(tile, (width*x, height*y, width*(x+1), height*(y+1)))
			print ("Downloading: {}/{}".format(x*level + y + 1, level*level), end="\r")

	print("\nFinished\n")

	if outfile == '':
		outfile = strftime("%Y-%m-%d-%H%M%S",latest) + ".png"

	if outfile[-4:] == ".png":
		img.save(outfile, "PNG")
	elif outfile[-4:] == ".jpg":
		img.save(outfile, "JPEG")
	elif outfile[-4:] == ".bmp":
		img.save(outfile, "BMP")
	elif outfile[-5:] == ".tiff":
		img.save(outfile, "TIFF")
	elif outfile[-4:] == ".pcx":
		img.save(outfile, "PCX")
	elif outfile[-4:] == ".ppm":
		img.save(outfile, "PPM")
	else:		
		img.save(outfile + ".png", "PNG")

if __name__ == "__main__":
	main()