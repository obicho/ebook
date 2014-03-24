import unittest
from TxtReader import TxtReader

class TestTxtReader(unittest.TestCase):
    def testNextWord(self):
        fh = open('tests/txt_reader_test_file1.txt')
        fh2 = open('tests/txt_reader_test_file1.txt')
        r = TxtReader(fh)
        self.assertEquals('online', r.nextWord())
        self.assertWord('online', r.startPointer(), r.endPointer(), fh2)

        self.assertEquals('at', r.nextWord())
        self.assertWord('at', r.startPointer(), r.endPointer(), fh2)

        self.assertEquals('www.gutenberg.org', r.nextWord())
        self.assertWord('www.gutenberg.org', r.startPointer(), r.endPointer(), fh2)

        self.assertEquals('\n', r.nextWord())
        self.assertWord('\n', r.startPointer(), r.endPointer(), fh2)

        self.assertEquals('Title:', r.nextWord())
        self.assertWord('Title:', r.startPointer(), r.endPointer(), fh2)

    def assertWord(self, word, s, e, fh):
        fh.seek(s)
        self.assertEquals(word, fh.read(e - s))

    def testNextWordEntireBook(self):
        fh = open('sense.txt')
        fh2 = open('sense.txt')
        r = TxtReader(fh)
        while True:
            word = r.nextWord()
            if word == None:
                break
            else:
                self.assertWord(word, r.startPointer(), r.endPointer(), fh2)

if __file__ == '__main__':
    unittest.main()

