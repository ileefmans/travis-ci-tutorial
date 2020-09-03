import unittest
from calc import Calc

class Test(unittest.TestCase):
    
    
    def test_add(self):
        result = Calc(1,2).add()
        self.assertEqual(3, result)
    
    def test_subtract(self):
        result = Calc(1,2).subtract()
        self.assertEqual(-1, result)
    
    def test_multiply(self):
        result = Calc(1,2).multiply()
        self.assertEqual(2, result)
    
    def test_divide(self):
        result = Calc(1,1).divide()
        self.assertEqual(1, result)


if __name__ == '__main__':
    unittest.main()
