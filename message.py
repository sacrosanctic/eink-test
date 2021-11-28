
#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
imgdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
form lib import epd7in5b_V2
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
    #epd.Clear()

    font48 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'),48)
    font36 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 36)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    fontbig = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 72)

    logging.info("3.read bmp file")
    Himage = Image.open(os.path.join(imgdir, 'message.png'))
    Himage_Other = Image.new('1', (epd.height, epd.width), 255)
    epd.display(epd.getbuffer(Himage),epd.getbuffer(Himage_Other))

    logging.info("Clear...")
    #epd.init()
    #epd.Clear()

    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in5b_V2.epdconfig.module_exit()
    exit()
