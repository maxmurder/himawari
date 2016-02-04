#!/usr/bin/env python3

from io import BytesIO
from json import loads
from time import strptime, strftime
from PIL import Image
from urllib.request import urlopen

level = 20

def main():
	height = 550;
	width = 550;

	with urlopen("http://himawari8-dl.nict.go.jp/himawari8/img/D531106/latest.json") as latest_json:	
		latest = strptime(loads(latest_json.read().decode("utf-8"))["date"], "%Y-%m-%d %H:%M:%S")

	print("Latest: {} GMT\n".format(strftime("%Y/%m/%d/%H:%M:%S",latest)))

	url_format = "http://himawari8.nict.go.jp/img/D531106/{}d/{}/{}_{}_{}.png"

	png = Image.new('RGB',(width*level, height*level))

	print("Downloading: 0/{}".format(level*level), end="\r")

	for x in range(level):
		for y in range(level):
			with urlopen(url_format.format(level,width,strftime("%Y/%m/%d/%H%M%S",latest), x, y)) as tile_w:
				tileData = tile_w.read()

			tile = Image.open(BytesIO(tileData))

			png.paste(tile, (width*x, height*y, width*(x+1), height*(y+1)))
			print ("Downloading: {}/{}".format(x*level + y + 1, level*level), end="\r")

	print("Finished")

	png.save(strftime("%Y-%m-%d-%H%M%S",latest) + ".png", "PNG")

if __name__ == "__main__":
	main()