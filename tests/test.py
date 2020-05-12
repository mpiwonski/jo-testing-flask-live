import unittest
from fractions import Fraction


class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEquals(result, 6)
        print('Chyba się udało!')

    def test_list_fraction(self):
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEquals(result, 1)



if __name__ == 'main':
    unittest.main()