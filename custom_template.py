
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

    # Drawing scott's image
    logging.info("Drawing scott's image...")

    black = Image.new('1', (epd.width, epd.height), 255)
    red = Image.new('1', (epd.width, epd.height), 255)
    draw_black = ImageDraw.Draw(black)
    draw_red = ImageDraw.Draw(red)

    today = date.today().strftime('%Y年%m月%d日')

    draw_red.text((10,0), today+"藍雅歌" ,font = font48, fill = 0)

    draw_black.line((0,60,800,60), fill = 0)
    draw_black.text((10,60),"Projects", font = font36, fill = 0)
    draw_black.text((11, 120), "-Tuition and Pay Chart for 管乐公司",font = font24, fill = 0)
    draw_black.text((11,150), "-New scholarship format", font = font24, fill = 0)
    draw_red.text((11,180), "-Contact 麦子 and 德惠", font = font24, fill = 0)

    draw_black.line((400,60,400,480), fill = 0)
    draw_black.text((411,60), "Calendar", font = font36, fill = 0)
    draw_red.text((411,100), "Today", font = font24, fill = 0)
    draw_black.text((411,200), "Next 7 days", font = font24, fill = 0)
    draw_black.text((410,300), "Next 30 days", font = font24, fill = 0)

    draw_black.text((410,130), "ABC Orchestra Perforamance at the xyx Threater", font = font18, fill = 0)
    draw_black.text((410,230), "惠宝 Final's Exam", font = font18, fill = 0)

    epd.display(epd.getbuffer(black),epd.getbuffer(red))

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
