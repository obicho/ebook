# Emulating e-ink display on a 2.7 inch display
# Loads a book from text file
# Reads line by line and print them a pageful at a time

import textwrap, re
import codecs
import Image, ImageFont, ImageDraw

# Setup
font = ImageFont.load_default()
LEFT_MARGIN = 5
w, h = (264, 176)
HEIGHT = 11
wrapper = textwrap.TextWrapper(replace_whitespace = False, width = 40)

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
		print '-------------'
		print paragraph

		lines = wrapper.wrap(paragraph)
		for line in lines:
			simpleLine = cleanse(line)
			draw.text((LEFT_MARGIN, y_text), simpleLine, font = font, fill = 'black')
			y_text += HEIGHT
		y_text += HEIGHT #generating a line between paragraphs
	bg.show()
	bg.save('test.png')




# Main function starts here
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


