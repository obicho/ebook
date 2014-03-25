class StopWords:
    def __init__(self):
        self.__stop_words = set()
        self._load_stop_words()

    def _load_stop_words(self):
        with open('resources/stopwords.txt') as f:
            for word in f.read().split('\n'):
                self.__stop_words.add(word.strip())

    def is_stop_word(self, word):
        return word in self.__stop_words

