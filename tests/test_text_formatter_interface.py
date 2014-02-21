import unittest
import TextFormatterInterface

class TestTextFormatterInterface(unittest.TestCase):

    def setUp(self):
        bookFile = open("sense.txt")
        self.t = TextFormatterInterface.new(bookFile, 264, 176)

    def testLoadBook(self):
        len(self.t.page_pointer) > 0

if __name__ == '__main__':
    unittest.main()
