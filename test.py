import unittest
import countMethods

class TestCalc(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(countMethods.count('2+2'),'4')
    def test_add_neg_and_pos(self):
        self.assertEqual(countMethods.count('-2+2'),'0')
    def test_add_poz_and_neg(self):
        self.assertEqual(countMethods.count('2+-2'),'0')
    def test_sub_positive(self):
        self.assertEqual(countMethods.count('2-2'),'0')

if __name__ == '__main__':
    unittest.main()