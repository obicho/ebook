from collections import deque

class TxtReader:
    def __init__(self, fh):
        self.__fh = fh
        self.__words = deque()
        self.__pointer = 0
        self.__current_word = None

    def nextWord(self):
        if len(self.__words)==0 and not self.__add_words():
            return None
        self.__current_word = self.__words.popleft()
        return self.__current_word[0]

    def __add_words(self):
        line = self.__fh.readline()
        if line == '':
            return False
        
        if line == '\n' or line == '\r\n':
            self.__words.append(('\n', self.__pointer, self.__pointer+len(line)))
            self.__pointer += len(line)
        else:
            if line[-1] == '\n':
                line = line[0:-1]

            words = line.split(' ')
            for word in words:
                l = len(word)
                self.__words.append((word.replace('\r',''), self.__pointer, self.__pointer+l))
                self.__pointer += l + 1

        return True


    def startPointer(self):
        return self.__current_word[1]

    def endPointer(self):
        return self.__current_word[2]

    def seek(self, pointer):
        self.__pointer = pointer
        self.__fh.seek(pointer)
        self.__words.clear()
