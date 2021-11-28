
#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from lib import epd7in5b_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

import requests
import shutil
from datetime import date

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd7in5b_V2 Demo")

    epd = epd7in5b_V2.EPD()
    logging.info("init and Clear")
    epd.init()

    # get image from local server
    test = requests.get("http://192.168.31.53:5000/download.jpeg", stream=True)
    with open('img.png','wb') as out_file:
        shutil.copyfileobj(test.raw, out_file)
    del test
    imgBlack = Image.open('img.png')
    imgRed = Image.new('1', (epd.height, epd.width), 255)
    epd.display(epd.getbuffer(imgBlack),epd.getbuffer(imgRed))

    logging.info("Goto Sleep...")
    epd.sleep()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd7in5b_V2.epdconfig.module_exit()
    exit()
