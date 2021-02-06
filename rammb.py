import os
import logging
import json
from time import strptime, strftime
from urllib.request import Request, urlopen
from urllib.error import URLError
from PIL import Image
from io import BytesIO

logging.getLogger().setLevel(logging.INFO)

COLO_BASE_URL = 'https://rammb-slider.cira.colostate.edu/data/'
TILE_WIDTH = 678
ZOOM_TILES = [1, 2, 4, 8, 16]


def get_latest_url(sat='goes-17',sector='full_disk', product='geocolor'):
    """
    Get latest image url
    :param sat: which satellite to get images from (goes-16, goes-17, himawari, jpss)
    :param product:
    :return:
    """
    timestamps_url = f'{COLO_BASE_URL}json/{sat}/{sector}/{product}/latest_times.json'
    request = Request(timestamps_url)
    try:
        result = urlopen(request)
        latest_times = json.loads(result.read().decode('utf-8'))
        latest_timestamp = latest_times.get('timestamps_int')[0]
        latest_datetime = strptime(str(latest_timestamp), '%Y%m%d%H%M%S')
        logging.info(f'Latest {strftime("%Y/%m/%d %H:%M:%S", latest_datetime)}')
        return f'{COLO_BASE_URL}imagery/{strftime("%Y%m%d", latest_datetime)}/{sat}---{sector}/{product}/{latest_timestamp}/', latest_datetime
    except URLError as err:
        logging.error(f'Request failed: {err.code} {err.reason}')


def get_image_url(zoom=0, tile_x=0, tile_y=0, latest_url=None):
    """
    Get rammb image url
    :param zoom: zoom level 00-04
    :param tile_x: x tile of image to retrieve
    :param tile_y: y tile of image to retrieve
    :param latest_url: url of latest image timestamp
    :return:
    """
    if not latest_url:
        latest_url = get_latest_url()
    return f'{latest_url}{zoom:02}/{tile_y:03}_{tile_x:03}.png'


def get_latest_image_urls(sat='goes-17', sector='full_disk', product='geocolor', zoom=0):
    latest_url, latest_datetime = get_latest_url(sat=sat, sector=sector, product=product)
    urls = list()
    for tile_x in range(0, ZOOM_TILES[zoom]):
        for tile_y in range(0, ZOOM_TILES[zoom]):
            urls.append(dict(url=get_image_url(zoom=zoom, tile_x=tile_x, tile_y=tile_y, latest_url=latest_url),
                        tile_x=tile_x, tile_y=tile_y))
    return urls, latest_datetime


def download_image(url):
    request = Request(url)
    try:
        result = urlopen(request)
        return result.read()
    except URLError as err:
        logging.error(f'Request failed: {err.code} {err.reason}')


def download_latest_image(sat='goes-17', sector='full_disk', product='geocolor', zoom=0, output_dir=None, filename=None):
    zoom = min(4, zoom)
    tiles, latest_datetime = get_latest_image_urls(sat=sat, sector=sector, product=product, zoom=zoom)
    image_width = TILE_WIDTH * ZOOM_TILES[zoom]
    image = Image.new('RGB', (image_width, image_width))
    logging.debug(f'Created image: {image.size}')
    n = 0
    for tile_info in tiles:
        n += 1
        logging.info(f'Downloading image {n} of {len(tiles)}')
        logging.debug(tile_info.get("url"))
        tile_data = download_image(tile_info.get('url'))
        if tile_data:
            tile = Image.open(BytesIO(tile_data))
            tile_box = (TILE_WIDTH * tile_info.get('tile_x'),
                        TILE_WIDTH * tile_info.get('tile_y'),
                        TILE_WIDTH * (tile_info.get('tile_x') + 1),
                        TILE_WIDTH * (tile_info.get('tile_y') + 1))
            image.paste(tile, tile_box)
    if not filename:
        filename = strftime(f'{sat}_{sector}_{product}_%Y-%m-%d-%H%M%S.png', latest_datetime)
    if not output_dir:
        output_dir = os.getcwd()
    out_path = os.path.join(output_dir, filename)
    logging.info(f'Saving: {out_path}')
    image.save(out_path, 'PNG')



