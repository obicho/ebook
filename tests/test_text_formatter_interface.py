import unittest
from TextFormatterInterface import TextFormatterInterface

class TestTextFormatterInterface(unittest.TestCase):

    def setUp(self):
        bookFile = open("sense.txt")
        self.t = TextFormatterInterface(bookFile, 45, 20)

    def testLoadBook(self):
        self.assertGreater(len(self.t.page_pointer), 10)

    def testGetPage(self):
        # print self.t.getPage(0)
        self.assertGreater(len(self.t.getPage(0)), 100)

if __name__ == '__main__':
    unittest.main()
