from TxtReader import TxtReader
import codecs

class TextFormatterInterface:
    def __init__ (self, book_handle, width, height):
        self.width = width
        self.height = height
        self.book_handle = book_handle
        self.loadBook()

    def loadBook(self):
        self.__current_page_id = 0
        self.page_pointer = []
        self.__reader = TxtReader(self.book_handle)
        self.__reader.seek(0)
        offset = 0
        while True:
            page = self._getPageByPointer(offset)
            if page == None:
                break

            self.page_pointer.append(offset)
            new_offset = self.__reader.startPointer()

            if new_offset == offset:
                break
            else:
                offset = new_offset

    def getPage(self, page_id):
        if page_id < 0 or page_id >= self.pageCount():
            raise ValueError("Invalid page_id: " + page_id)

        pointer = self.page_pointer[page_id]
        return self._getPageByPointer(pointer)

    def _getPageByPointer(self, pointer):
        self.__reader.seek(pointer)
        lines = []
        line = self.__reader.nextWord()

        while True:
            word = self.__reader.nextWord()
            if word == None:
                break

            if word == '\n' or len(line) + len(word) + 1 > self.width:
                lines.append(self.cleanse(line))
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
