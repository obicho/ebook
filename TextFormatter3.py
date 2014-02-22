

import sys, codecs
from EPD import EPD
import textwrap, re
import Image, ImageFont, ImageDraw


# Setup
WHITE = 1
BLACK = 0
#font = ImageFont.load_default()
font = ImageFont.truetype("simhei.ttf")
LEFT_MARGIN = 5

w, h = (264, 176)
HEIGHT = 11
wrapper = textwrap.TextWrapper(replace_whitespace = False, width = 40)
epd = EPD()

def main(argv):
   
    

    print('panel = {p:s} {w:d} x {h:d}  version={v:s}'.format(p=epd.panel, w=epd.width, h=epd.height, v=epd.version))

    epd.clear()

 #   bookFile = open("sense.txt")
    bookFile = codecs.open('ch.txt', encoding='utf-8')
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
            #simpleLine = cleanse(line)
            simpleLine = line
            draw.text((LEFT_MARGIN, y_text), simpleLine, font = font, fill = 'black')
            y_text += HEIGHT
        y_text += HEIGHT #generating a line between paragraphs
    #bg.show()
    #bg.save('test.png')
    epd.display(bg)
    epd.update()

# main
if "__main__" == __name__:
    if len(sys.argv) < 1:
        sys.exit('usage: {p:s}'.format(p=sys.argv[0]))
    main(sys.argv[1:])
