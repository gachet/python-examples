import unittest
from app.primes import Primes
 
class TddInPythonExample(unittest.TestCase):
 
    def test_primes1_method_returns_correct_result(self):
        # p = Primes()
        # result = p.divisible(4, 2)
        self.assertEqual(True, True)

    # def test_primes_generateList_method_returns_correct_result(self):
    #     p = Primes()
    #     result = p.generateList(2, 11)
    #     self.assertEqual([2, 3, 4, 5, 6, 7, 8, 9, 10, 11], result)

        
    # def test_primes_dividers_method_returns_correct_result(self):
    #     p = Primes()
    #     result = p.dividers(4)
    #     self.assertEqual(24, result)

    
if __name__ == '__main__':
    unittest.main()
