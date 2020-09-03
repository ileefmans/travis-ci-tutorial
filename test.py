import unittest
from calc import Calc

class Test(unittest.TestCase):
    
    
    def case1(self):
        result = Calc(1,2).add()
        self.assertEqual(result,3)
    
    def case2(self):
        result = Calc(1,2).subtract()
        self.assertEqual(result, -1)
    
    def case3(self):
        result = Calc(1,2).multiply()
        self.assertEqual(result,2)
    
    def case4(self):
        result = Calc(1,0).divide()
        self.assertEqual(result,0)


if __name__ == '__main__':
    Test.main()
