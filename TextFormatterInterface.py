class TextFormatterInterface:
    def __init__ (self, book_handle, width, height):
        self.width = width
        self.height = height
        self.book_handle = book_handle
        self.page_pointer = []
        self.loadBook()
        self.
        self.wrapper = textwrap.TextWrapper(replace_whitespace = False, width = 40)

    def loadBook():
        self.book_handle.seek(0)
        offset = 0
        page_line = 0
        self.page_pointer.append(0)

        #TODO record the starting position of every page based on screen size
        for line in book_handle:
            offset += len(line)
            if page_line >= 20:
                self.page_pointer.append(offset)
                page_line = 0

    def cleanse(self, line):
        newline = line
        if (line.startswith(codecs.BOM_UTF8)):
            newline = line[3:]
    
        return newline;

    def drawScreen(self, text):
        bg = Image.new('RGBA', (w, h), "#FFFFFF")
        draw = ImageDraw.Draw(bg)
        y_text = 10

        #feed textwrap one paragraph at a time. accomodate for carriage return, newline various os
        for paragraph in re.split('\r\n\r\n|\n\n', text): 
            lines = self.wrapper.wrap(paragraph)
            for line in lines:
                simpleLine = cleanse(line)
                draw.text((LEFT_MARGIN, y_text), simpleLine, font = font, fill = 'black')
                y_text += HEIGHT
            y_text += HEIGHT #generating a line between paragraphs

    def drawPage(self):
        self.nextPage()
        # code

    def nextPage(self):
        # self.file_h
