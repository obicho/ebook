from Queue import Queue

class TxtReader:
    def __init__(self, fh):
        self.__fh = fh
        self.__fh.seek(0)
        self.__words = Queue()
        self.__pointer = 0
        self.__current_word = None

    def nextWord(self):
        if self.__words.empty() and not self.__add_words():
            return None
        self.__current_word = self.__words.get()
        return self.__current_word[0]

    def __add_words(self):
        line = self.__fh.readline()
        if line == '':
            return False
        
        if line == '\n':
            self.__words.put(('\n', self.__pointer, self.__pointer+1))
            self.__pointer += 1
        else:
            if line[-1] == '\n':
                line = line[0:-1]

            words = line.split(' ')
            for word in words:
                l = len(word)
                self.__words.put((word, self.__pointer, self.__pointer+l))
                self.__pointer += l + 1

        return True


    def startPointer(self):
        return self.__current_word[1]

    def endPointer(self):
        return self.__current_word[2]
