import unittest

class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEquals(result, 6)
        print('Chyba się udało!')

if __name__ == 'main':
    unittest.main()