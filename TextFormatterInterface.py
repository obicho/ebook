from TxtReader import TxtReader
from TxtIndex import TxtIndex
import codecs
import bisect

class TextFormatterInterface:
    def __init__ (self, book_handle, width, height):
        self.width = width
        self.height = height
        self.book_handle = book_handle
        self.loadBook()
        self.loadIndex()

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

    def loadIndex(self):
        self.__index = TxtIndex(self.book_handle)

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

    def search(self, phrase):
        pointers = self.__index.exact_search(phrase)
        if pointers == None:
            return None

        page_nums = []
        for pointer in pointers:
            page_num = self.getPageNumFromPointer(pointer)
            if (len(page_nums) == 0 or page_nums[-1] != page_num):
                page_nums.append(page_num)

        return page_nums

    def getPageNumFromPointer(self, pointer):
        return bisect.bisect_right(self.page_pointer, pointer)

    def fuzzySearch(self, phrase):
        word_pointers = self.__index.get_word_pointers(phrase)
        if word_pointers == None:
            return None

        page_word_count = {}
        for word in word_pointers:
            pointers = word_pointers[word]
            if pointers == None:
                continue

            for pointer in pointers:
                page_num = self.getPageNumFromPointer(pointer)
                if page_num not in page_word_count:
                    page_word_count[page_num] = {}

                if word not in page_word_count[page_num]:
                    page_word_count[page_num][word] = 0

                page_word_count[page_num][word] += 1

        pages_ranked = sorted(page_word_count.items(), key=self.__pageCompare)
        pages_ranked = [x[0] for x in pages_ranked]

        if pages_ranked == []:
            return None

        return pages_ranked

    def __pageCompare(self, page_word_count):
        page, word_count = page_word_count
        # sort page first by number occurences of unique word, 
        # then by total count in descending order
        # then by page number in ascending order
        return (-len(word_count), -sum(word_count.values()), page)

