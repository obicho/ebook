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

    def testGetPageNavigate(self):
        p1 = self.t.getPage(50)
        p2 = self.t.getPage(50)
        self.assertEquals(p1, p2)

    def testGetPageNavigate2(self):
        p1 = self.t.getPage(50)
        p2 = self.t.getPage(51)
        p3 = self.t.getPage(50)
        p4 = self.t.getPage(51)
        self.assertEquals(p1, p3)
        self.assertEquals(p2, p4)

    def testGetPageSimpleIntegrityCheck(self):
        self.t.getPage(0)
        pages = ''
        for i in range(10):
            pages += self.t.getPage(i)

        fh = open('sense.txt')
        original = fh.read(len(pages)*2)

        original = self.t.cleanse(original.replace('\r\n', '').replace('\n', '').replace(' ', ''))
        pages = pages.replace('\n', '').replace(' ', '')
        # print ''
        # print 'pages: \n' + pages
        # print '-'*20
        # print 'original: \n' + original

        self.assertTrue(original.startswith(pages))

    def testSearch(self):
        page_nums = self.t.search('elinor')
        self.assertNotEquals(page_nums, None)
        for page_num in page_nums:
            page = self.t.getPage(page_num-1)
            self.assertTrue('elinor' in page.lower(), 'elinor is not found in %s' % (page,))

if __name__ == '__main__':
    unittest.main()
