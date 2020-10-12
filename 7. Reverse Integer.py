# Solution for problem #7 `Reverse Integer`
#
# Description: Given a 32-bit signed integer, reverse digits of an integer.
#
# Assume we are dealing with an environment that could only store integers 
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose 
# of this problem, assume that your function returns 0 when the reversed 
# integer overflows.
import unittest

class Solution:
    def reverse(self, x: int) -> int:
        result = str(x)[::-1]

        if result[-1] == '-':
            result = '-' + result[:-1]

        r = int(result)

        if (r > 2**31-1) or (r < -2**31):
            return 0
        else:
            return r

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