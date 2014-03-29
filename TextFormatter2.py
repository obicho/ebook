

import sys, codecs
import textwrap, re
import Image, ImageFont, ImageDraw
from TextFormatterInterface import TextFormatterInterface

# Setup
WHITE = 1
BLACK = 0
font = ImageFont.load_default()
LEFT_MARGIN = 5
w, h = (264, 176)
WIDTH = 40
HEIGHT = 14
LINE_HEIGHT = 11

def main():
    bookFile = open("sense.txt")
    pages = TextFormatterInterface(bookFile, WIDTH, HEIGHT)
    print("This book has %d pages" % (pages.pageCount(),))
    page_id = -1

    while True:
        try:
            print '-'*WIDTH
            page_num = raw_input("<Enter> next page\n<Page number> jump to a page\n</string> exact search\n: ")
            if page_num == '':
                page_id += 1
            elif page_num[0] == '/':
                page_nums = pages.search(page_num[1:])
                print "found '%s' in the following pages: %s" % (page_num[1:], page_nums)
                if page_nums == None:
                    continue

                page_id = int(page_nums[0])-1
            else:
                page_id = int(page_num)-1

            page = pages.getPage(page_id)
            print page
            drawPage(page)
        except Exception as e:
            print 'Failed to query page num: %s' % (page_num,)
            print e

# Draws a screen full (page) of text
def drawPage(text):
    bg = Image.new('RGBA', (w, h), "#FFFFFF")
    draw = ImageDraw.Draw(bg)
    y_text = 10

    #feed textwrap one paragraph at a time. accomodate for carriage return, newline various os
    for line in text.split('\n'):
        draw.text((LEFT_MARGIN, y_text), line, font = font, fill = 'black')
        y_text += LINE_HEIGHT
    bg.show()
    bg.save('test.png')
    # epd.display(bg)
    # epd.update()

# main
if __name__ == "__main__":
    main()
