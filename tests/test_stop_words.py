import unittest
from StopWords import StopWords

class TestStopWords(unittest.TestCase):
    def setUp(self):
        self.s = StopWords()

    def testIsStopWord(self):
        self.assertTrue(self.s.is_stop_word('a'))

    def testIsStopWord2(self):
        self.assertFalse(self.s.is_stop_word('rare word'))
