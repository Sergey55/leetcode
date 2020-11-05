"""Solution for problem #29. Divide Two Integers

Description: Given two integers dividend and divisor, divide two 
integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing 
its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:

    Assume we are dealing with an environment that could only store 
    integers within the 32-bit signed integer range: [−231,  231 − 1]. 
    For this problem, assume that your function returns 231 − 1 when 
    the division result overflows.
"""

import unittest

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return float('inf')
        
        sign = 1 if (dividend > 0) == (divisor > 0) else -1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
                
        power = 1
        
        current_dividend = dividend
        current_divisor = divisor
        
        while current_dividend > current_divisor:
            current_dividend -= current_divisor
            power += power
            current_divisor += current_divisor
            
        result = 0
        
        while power >= 1:
            if dividend >= current_divisor: 
                dividend -= current_divisor
                result += power
            power >>= 1
            current_divisor >>= 1
        
        result = sign * result
            
        return min((2**31 - 1), result) if result >= 0 else max(-2**31, result)

class TestsForSolution(unittest.TestCase):
    def test_no_1(self):
        dividend, divisor = 10, 3
        output = 3

        solution = Solution()
        self.assertEqual(output, solution.divide(dividend, divisor))

    def test_no_2(self):
        dividend, divisor = 7, -3
        output = -2

        solution = Solution()
        self.assertEqual(output, solution.divide(dividend, divisor))

    def test_no_3(self):
        dividend, divisor = 0, 1
        output = 0

        solution = Solution()
        self.assertEqual(output, solution.divide(dividend, divisor))

    def test_no_4(self):
        dividend, divisor = 1, 1
        output = 1

        solution = Solution()
        self.assertEqual(output, solution.divide(dividend, divisor))

if __name__ == '__main__':
    unittest.main()