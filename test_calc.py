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
    
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            Calc(3,0).divide()



if __name__ == '__main__':
    unittest.main()
