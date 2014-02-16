# Emulating e-ink display on a 2.7 inch display
# Loads a book from text file
# Reads line by line and print them a pageful at a time

import textwrap
import Image, ImageFont, ImageDraw


font = ImageFont.load_default()
LEFT_MARGIN = 5
w, h = (264, 176)

# Draws a screen full (page) of text
def drawPage(text):
	bg = Image.new('RGBA', (w, h), "#FFFFFF")
	draw = ImageDraw.Draw(bg)
	lines = textwrap.wrap(text, width = 40)
	y_text = 10
	for line in lines:
	    width, height = font.getsize(line)
	    draw.text((LEFT_MARGIN, y_text), line, font = font, fill = 'black')
	    y_text += height
	bg.show()
	bg.save('test.png')

bookFile = open("s.txt")

lineBucket = ''

for bookFileLine in bookFile :

	if len(lineBucket) < 300:
		lineBucket+=bookFileLine
	else:
		print len(lineBucket)
		print lineBucket
		lineBucket+=bookFileLine #got to add this or you will miss a line
		drawPage(lineBucket)
		lineBucket = ''
		raw_input('any key to continue')

bookFile.close()

#Output remaining text if any
if len(lineBucket) > 0:
	drawPage(lineBucket)


