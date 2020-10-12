# Solution for problem #7 `Reverse Integer`
#
# Description: Given a 32-bit signed integer, reverse digits of an integer.
#
# Assume we are dealing with an environment that could only store integers 
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose 
# of this problem, assume that your function returns 0 when the reversed 
# integer overflows.
#
# Score: Runtime: 24 ms, faster than 96.73% of Python3 online submissions for Reverse Integer.
# Memory Usage: 14.1 MB, less than 99.98% of Python3 online submissions for Reverse Integer.

import unittest

class Solution:
    def reverse(self, x: int) -> int:
        result = 0

        temp_x = abs(x)

        while temp_x:
            result = result * 10 + temp_x % 10
            temp_x //= 10

        if (result < -2**31) or (result > 2**31 - 1):
            return 0

        return result if x > 0 else -1 * result

class TestsForSolution(unittest.TestCase):

    def test_no_1(self):
        inputValue = 123
        outputValue = 321

        solution = Solution()
        self.assertEqual(outputValue, solution.reverse(inputValue))

    def test_no_2(self):
        inputValue = -123
        outputValue = -321

        solution = Solution()
        self.assertEqual(outputValue, solution.reverse(inputValue))
        
    def test_no_3(self):
        inputValue = 120
        outputValue = 21

        solution = Solution()
        self.assertEqual(outputValue, solution.reverse(inputValue))

    def test_no_4(self):
        inputValue = 0
        outputValue = 0

        solution = Solution()
        self.assertEqual(outputValue, solution.reverse(inputValue))

    def test_no_5(self):
        inputValue = 1534236469
        outputValue = 0

        solution = Solution()
        self.assertEqual(outputValue, solution.reverse(inputValue))    

if __name__ == '__main__':
    unittest.main()