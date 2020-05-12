import unittest
from fractions import Fraction


class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEquals(result, 6)
        print('Chyba się udało!')

    def test_list_fraction(self):
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 4)]
        result = sum(data)
        self.assertEquals(result, 1)

    def test_bad_type(self):
        data = 'banana'
        with self.assertRaises(TypeError):
            sum(data)



if __name__ == 'main':
    unittest.main()