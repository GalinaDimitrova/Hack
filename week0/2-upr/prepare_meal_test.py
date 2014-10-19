import unittest
from prepare_meal import prepare_meal


class CashDeskTest(unittest.TestCase):

    def test_prepare_meal(self):
        self.assertEqual('spam', prepare_meal(3))
        self.assertEqual('spam spam spam', prepare_meal(27))
        self.assertEqual('', prepare_meal(7))

if __name__ == '__main__':
    unittest.main()
