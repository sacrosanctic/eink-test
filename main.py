
#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
import epd7in5b_V2
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

    '''
    black2 = Image.new('1', (epd.width, epd.height), 255)
    red2 = Image.new('1', (epd.width, epd.height), 255)
    draw_black2 = ImageDraw.Draw(black2)
    draw_red2 = ImageDraw.Draw(red2)
    draw_red2.text((220,200),"Sasha, I love you", font = fontbig, fill = 0)
    epd.display(epd.getbuffer(black2),epd.getbuffer(red2))
    '''


    '''
    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...")
    Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    Other = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    draw_Himage = ImageDraw.Draw(Himage)
    draw_other = ImageDraw.Draw(Other)
    draw_Himage.text((10, 0), 'hello world', font = font24, fill = 0)
    draw_Himage.text((10, 20), '7.5inch e-Paper', font = font24, fill = 0)
    draw_Himage.text((150, 0), u'微雪电子', font = font24, fill = 0)    
    draw_other.line((20, 50, 70, 100), fill = 0)
    draw_other.line((70, 50, 20, 100), fill = 0)
    draw_other.rectangle((20, 50, 70, 100), outline = 0)
    draw_other.line((165, 50, 165, 100), fill = 0)
    draw_Himage.line((140, 75, 190, 75), fill = 0)
    draw_Himage.arc((140, 50, 190, 100), 0, 360, fill = 0)
    draw_Himage.rectangle((80, 50, 130, 100), fill = 0)
    draw_Himage.chord((200, 50, 250, 100), 0, 360, fill = 0)
    epd.display(epd.getbuffer(Himage),epd.getbuffer(Other))
    time.sleep(30)

    # Drawing on the Vertical image
    logging.info("2.Drawing on the Vertical image...")
    Limage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    Limage_Other = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw_Himage = ImageDraw.Draw(Limage)
    draw_Himage_Other = ImageDraw.Draw(Limage_Other)
    draw_Himage.text((2, 0), 'hello world', font = font18, fill = 0)
    draw_Himage.text((2, 20), '7.5inch epd', font = font18, fill = 0)
    draw_Himage_Other.text((20, 50), u'微雪电子', font = font18, fill = 0)
    draw_Himage_Other.line((10, 90, 60, 140), fill = 0)
    draw_Himage_Other.line((60, 90, 10, 140), fill = 0)
    draw_Himage_Other.rectangle((10, 90, 60, 140), outline = 0)
    draw_Himage_Other.line((95, 90, 95, 140), fill = 0)
    draw_Himage.line((70, 115, 120, 115), fill = 0)
    draw_Himage.arc((70, 90, 120, 140), 0, 360, fill = 0)
    draw_Himage.rectangle((10, 150, 60, 200), fill = 0)
    draw_Himage.chord((70, 150, 120, 200), 0, 360, fill = 0)
    epd.display(epd.getbuffer(Limage), epd.getbuffer(Limage_Other))
    time.sleep(30)

    logging.info("3.read bmp file")
    Himage = Image.open(os.path.join(picdir, '7in5_V2_b.bmp'))
    Himage_Other = Image.open(os.path.join(picdir, '7in5_V2_r.bmp'))
    epd.display(epd.getbuffer(Himage),epd.getbuffer(Himage_Other))
    time.sleep(30)

    logging.info("4.read bmp file on window")
    Himage2 = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    Himage2_Other = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    bmp = Image.open(os.path.join(picdir, '2in9.bmp'))
    Himage2.paste(bmp, (50,10))
    Himage2_Other.paste(bmp, (50,300))
    epd.display(epd.getbuffer(Himage2), epd.getbuffer(Himage2_Other))
    time.sleep(30)
    '''

    '''
    # get image from local server
    Himage_other = Image.new('1', (epd.height, epd.width), 255)
    test = requests.get("http://192.168.31.53:5000/download.jpeg", stream=True)
    with open('img.png','wb') as out_file:
        shutil.copyfileobj(test.raw, out_file)
    del test
    Himage = Image.open('img.png')
    epd.display(epd.getbuffer(Himage),epd.getbuffer(Himage_other))
    '''

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
