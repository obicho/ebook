

import sys
import Image
import ImageDraw, ImageFont
from EPD import EPD
import textwrap

WHITE = 1
BLACK = 0

def main(argv):
    """main program - draw and display a test image"""

    epd = EPD()

    print('panel = {p:s} {w:d} x {h:d}  version={v:s}'.format(p=epd.panel, w=epd.width, h=epd.height, v=epd.version))

    epd.clear()

    demo(epd)


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
