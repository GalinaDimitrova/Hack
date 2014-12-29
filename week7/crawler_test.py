import unittest

from crawler import Crawler


class CrawlerTest(unittest.TestCase):

    def setUp(self):
        self.test_crawler = Crawler("aladinfoods.bg")

    def test_crawler_init(self):
        self.assertEqual(self.test_crawler.scaned_url, [])
        self.assertEqual(self.test_crawler.domain, "aladinfoods.bg")

    def test_is_outgoing(self):
        self.assertFalse(self.test_crawler.is_outgoing("http://aladinfoods.bg"))

    def test_is_not_outgoing(self):
        self.assertTrue(self.test_crawler.is_outgoing("http://hackbulgaria.com"))

    # def test_is_valid(self):
    #     self.assertTrue(self.test_crawler.is_valid("http://aladinfoods.bg/menu"))

    # def test_is_not_valid(self):
    #     self.assertFalse(self.test_crawler.is_valid("http://hackbulgaria.com"))

if __name__ == '__main__':
    unittest.main()
