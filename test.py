import unittest
import countMethods

class TestCalc(unittest.TestCase):
    def test_count(self):
        self.assertEqual(countMethods.count('2+2'),'4')

if __name__ == '__main__':
    unittest.main()