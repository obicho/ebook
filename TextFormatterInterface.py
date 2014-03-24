from TxtReader import TxtReader

class TextFormatterInterface:
    def __init__ (self, book_handle, width, height):
        self.width = width
        self.height = height
        self.book_handle = book_handle
        self.page_pointer = []
        self.loadBook()
        self.__current_page_id = 0

    def loadBook(self):
        self.book_handle.seek(0)
        self.__reader = TxtReader(self.book_handle)
        offset = 0
        line_width = 0
        line_count = 0

        while True:
            word = self.__reader.nextWord()
            if word == None:
                break

            if word == '\n' or line_width + len(word) + 1 > self.width:
                line_width = 0
                line_count += 1
                if line_count == self.height:
                    line_count = 0
                    self.page_pointer.append(offset)
                    if word == '\n':
                        offset = self.__reader.endPointer()
                    else:
                        offset = self.__reader.startPointer()
                        line_width = len(word)
            else:
                if line_width == 0:
                    line_width = len(word)
                else:
                    line_width += len(word)+1

    def getPage(self, page_id):
        if page_id < 0 or page_id >= self.pageCount():
            raise ValueError("Invalid page_id: " + page_id)

        pointer = self.page_pointer[page_id]
        self.book_handle.seek(pointer)
        lines = []
        line = self.__reader.nextWord()

        while True:
            word = self.__reader.nextWord()
            if word == None:
                break

            if word == '\n' or len(line) + len(word) + 1 > self.width:
                lines.append(line)
                if len(lines) == self.height:
                    break
                if word == '\n':
                    line = ''
                else:
                    line = word
            else:
                line += ' ' + word

        return '\n'.join(lines)

    def cleanse(self, line):
        newline = line
        if (line.startswith(codecs.BOM_UTF8)):
            newline = line[3:]
    
        return newline;

    def getCurrentPage(self):
        return getPage(self.__current_page_id)

    def nextPage(self):
        self.__current_page_id += 1
        return getCurrentPage()

    def pageCount(self):
        return len(self.page_pointer)
