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
from lib import epd7in5b_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

import shutil
from datetime import date

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd7in5b_V2 Demo")

    epd = epd7in5b_V2.EPD()
    logging.info("init and Clear")
    epd.init()
    #epd.Clear()

    logging.info("3.read bmp file")
    blackimg = Image.open(os.path.join(imgdir, 'message.jpg'))
    redimg = Image.new('1', (epd.height, epd.width), 255)

    '''
    redimg = Image.open(os.path.join(imgdir,'message.png'))  # get image)
    rpixels = redimg.load()  # create the pixel map
    blackimg = Image.open(os.path.join(imgdir,'message.png')) # get image)
    bpixels = blackimg.load()  # create the pixel map

    for i in range(redimg.size[0]):  # loop through every pixel in the image
        for j in range(redimg.size[1]):
            if bpixels[i, j][0] > bpixels[i, j][1] and bpixels[i, j][0] > bpixels[i, j][2]:
              bpixels[i, j] = (255, 255, 255)  # change to white in the black image bitmap
            else:
              rpixels[i, j] = (255, 255, 255)  # change it to white in the red image bitmap

    '''
    epd.display(epd.getbuffer(blackimg),epd.getbuffer(redimg))

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
