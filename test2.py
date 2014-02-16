

import sys, codecs
from EPD import EPD
import textwrap, re
import Image, ImageFont, ImageDraw


# Setup
WHITE = 1
BLACK = 0
font = ImageFont.load_default()
LEFT_MARGIN = 5
w, h = (264, 176)
HEIGHT = 11
wrapper = textwrap.TextWrapper(replace_whitespace = False, width = 40)

def main(argv):
   
    epd = EPD()

    print('panel = {p:s} {w:d} x {h:d}  version={v:s}'.format(p=epd.panel, w=epd.width, h=epd.height, v=epd.version))

    epd.clear()

    bookFile = open("sense.txt")

    lineBucket = ''

    for bookFileLine in bookFile :

        if len(lineBucket) < 450:
            lineBucket+=bookFileLine
        else:
            lineBucket+=bookFileLine #got to add this or you will miss a line
            drawPage(lineBucket)
            lineBucket = ''
            raw_input('enter to continue')

    bookFile.close()

    #Output remaining text if any
    if len(lineBucket) > 0:
        drawPage(lineBucket)




# Remove unwanted, non-printable characters including BOM
def cleanse(line):
    newline = line
    if (line.startswith(codecs.BOM_UTF8)):
        print 'need cleansing'
        newline = line[3:]
    
    return newline;

# Draws a screen full (page) of text
def drawPage(text):
    bg = Image.new('RGBA', (w, h), "#FFFFFF")
    draw = ImageDraw.Draw(bg)
    y_text = 10

    #feed textwrap one paragraph at a time. accomodate for carriage return, newline various os
    for paragraph in re.split('\r\n\r\n|\n\n', text): 
        lines = wrapper.wrap(paragraph)
        for line in lines:
            simpleLine = cleanse(line)
            draw.text((LEFT_MARGIN, y_text), simpleLine, font = font, fill = 'black')
            y_text += HEIGHT
        y_text += HEIGHT #generating a line between paragraphs
    #bg.show()
    #bg.save('test.png')
    epd.display(bg)
    epd.update()

def demo(epd):
    """simple drawing demo - black drawing on white background"""
    # initially set all white background
    image = Image.new('1', epd.size, WHITE)
    # prepare for drawing
    draw = ImageDraw.Draw(image)
    w=200

    font = ImageFont.load_default() 

    text = "I've been reading through the Django Book, and in chapter 11 they talk about generating non-HTML content (such as PDF files, Images, RSS/Atom Feeds). They mention using PIL to generate images, but they don't give an example. So, I thought I'd post a simple example View that generates an image."
    lines = textwrap.wrap(text,width = 200)
    y_text =5 
    for line in lines:
  	width, height = font.getsize(line)
	draw.text(((w - width)/2, y_text), line,font=font, fill = 'black')
	y_text += height

    # display image on the panel
    epd.display(image)
    epd.update()


# main
if "__main__" == __name__:
    if len(sys.argv) < 1:
        sys.exit('usage: {p:s}'.format(p=sys.argv[0]))
    main(sys.argv[1:])
