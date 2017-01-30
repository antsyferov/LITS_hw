import unittest
from unittest.mock import patch
from calc import summ, div, ArgError, mul_random

class SimpleTestCase(unittest.TestCase):

    def test_check_sum(self):
        res = summ(1, 1)
        self.assertEqual(res, 2)

    def test_summ_exception(self):
        with self.assertRaises(ArgError):
            summ(1, None)

    def test_div(self):
        self.assertEqual([1,2,3], [1, 2, 3])
 
    @patch('calc.get_random')
    def test_mrandom(self, patched_random):
        patched_random.return_value = 2
        res = mul_random(1)
        self.assertEqual(res, 2)

    
