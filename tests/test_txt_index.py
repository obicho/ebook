import unittest
from TxtReader import TxtReader
from TxtIndex import TxtIndex

class TestTxtIndex(unittest.TestCase):
    def setUp(self):
        fh = open('sense.txt')
        self.index = TxtIndex(fh)

    def testStopWordsAreExcluded(self):
        self.assertEquals(None, self.index.get_pointers('a'))

    def testGetPointers(self):
        pointers = self.index.get_pointers('sense')
        fh = open('sense.txt')
        self.assertGreater(len(pointers), 10)
        for pointer in pointers:
            fh.seek(pointer)
            found = fh.read(len('sense'))
            self.assertEquals(self.index.norm_word(found), 'sense')

    def testGetPointersIgnoreCase(self):
        pointers_lower_case = self.index.get_pointers('sense')
        pointers_proper_case = self.index.get_pointers('Sense')
        pointers_all_cap = self.index.get_pointers('SENSE')
        self.assertEquals(len(pointers_lower_case), len(pointers_proper_case))
        self.assertEquals(len(pointers_proper_case), len(pointers_all_cap))

    def testExactSearch(self):
        phrase = 'a sense of duty'
        pointers = self.index.exact_search(phrase)
        self.assertNotEquals(pointers, None)
        fh = open('sense.txt')
        pointer = pointers[0]
        fh.seek(pointer)
        rs = fh.read(len(phrase))
        self.assertEquals(rs, phrase)

    def testExactSearchWithTrailingPunctuation(self):
        phrase = 'Elinor had no sense of fatigue'
        pointers = self.index.exact_search(phrase)
        self.assertNotEquals(pointers, None)
        fh = open('sense.txt')
        pointer = pointers[0]
        fh.seek(pointer)
        rs = fh.read(len(phrase))
        self.assertEquals(rs, phrase)
