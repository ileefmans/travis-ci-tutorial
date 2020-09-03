import unittest
from calc import Calc

class Test(unittest.TestCase):
    
    
    def case1(self):
        result = Calc(1,2).add()
        self.assertEqual(3, result)
    
    def case2(self):
        result = Calc(1,2).subtract()
        self.assertEqual(-1, result)
    
    def case3(self):
        result = Calc(1,2).multiply()
        self.assertEqual(2, result)
    
    def case4(self):
        result = Calc(1,0).divide()
        self.assertEqual(0, result)


#if __name__ == '__main__':
#unittest.main()
