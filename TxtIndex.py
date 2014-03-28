from TxtReader import TxtReader
from StopWords import StopWords
import re
import string

class TxtIndex:
    def __init__(self, fh):
        self.stop_words = StopWords()
        self.__fh = fh
        self.__reader = TxtReader(fh)
        self.build_index()

    def build_index(self):
        self.keyword2pointers = {}
        self.__reader.seek(0)

        while True:
            word = self.__reader.nextWord()
            if word == None:
                break

            word = self.norm_word(word)
            if self.stop_words.is_stop_word(word):
                continue

            if word not in self.keyword2pointers:
                self.keyword2pointers[word] = []

            self.keyword2pointers[word].append(self.__reader.startPointer())

    def norm_word(self, word):
        word = word.lower()
        word = word.rstrip(string.punctuation)
        return word

    def norm_phrase(self, phrase):
        phrase = re.sub('\s+', ' ', phrase)
        return ' '.join([self.norm_word(x) for x in phrase.split(' ')])

    def get_pointers(self, word):
        return self.keyword2pointers.get(self.norm_word(word))

    def exact_search(self, phrase):
        phrase = self.norm_phrase(phrase)
        words = phrase.split(' ')
        try_word = None
        try_word_idx = None
        try_word_pointers = []

        for i in range(len(words)):
            word = words[i]
            if self.stop_words.is_stop_word(word):
                continue

            pointers = self.get_pointers(word)
            if pointers == None:
                return None

            if try_word == None or len(try_word_pointers) > len(pointers):
                try_word = word
                try_word_idx = i
                try_word_pointers = pointers

        extend_left_by = len(' '.join(words[0:i])) + len(words[0:i])
        extend_right_by = len(' '.join(words[i:])) + len(words[i:])
        phrase_re = re.compile(phrase.replace(' ', '\s+'), re.I)
        found = []

        for pointer in try_word_pointers:
            s = pointer - extend_left_by
            l = extend_left_by + extend_right_by
            if s < 0:
                s = 0

            self.__fh.seek(s)
            excerpt = self.__fh.read(l)
            m = phrase_re.search(excerpt)
            if m:
                found.append(s + m.start())

        if len(found) > 0:
            return found
        else:
            return None
