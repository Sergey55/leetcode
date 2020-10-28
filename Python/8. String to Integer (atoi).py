# Solution for problem # 8 `String to Integer (atoi)`
#
# Description: Implement atoi which converts a string to an integer.
#
# The function first discards as many whitespace characters as necessary 
# until the first non-whitespace character is found. Then, starting from 
# this character takes an optional initial plus or minus sign followed by 
# as many numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the 
# integral number, which are ignored and have no effect on the behavior of 
# this function.
#
# If the first sequence of non-whitespace characters in str is not a valid 
# integral number, or if no such sequence exists because either str is empty 
# or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
# Note:
#   * Only the space character ' ' is considered a whitespace character.
#   * Assume we are dealing with an environment that could only store integers 
#   within the 32-bit signed integer range: [−2^31,  2^31 − 1]. If the numerical 
#   value is out of the range of representable values, INT_MAX (2^31 − 1) or 
#   INT_MIN (−2^31) is returned.
#
# Score: 
#   Runtime: 24 ms, faster than 98.50% of Python3 online submissions for String to Integer (atoi).
#   Memory Usage: 14.1 MB, less than 99.98% of Python3 online submissions for String to Integer (atoi).

import unittest

class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        i = 0
        sign = 1

        while (i < len(s) and s[i] == ' '):
            i += 1

        if i < len(s) and ((s[i] == '-') or (s[i] == '+')):
            sign = -1 if s[i] == '-' else 1
            i += 1

        for c in s[i:]:
            if c.isdigit():
                result = result * 10 + int(c)
            else:
                break

        result *= sign

        return min((2**31 - 1), result) if result >= 0 else max(-2**31, result)

class TestsForSolution(unittest.TestCase):
    def test_no_1(self):
        inputString = '42'
        output = 42

        solution = Solution()
        self.assertEqual(output, solution.myAtoi(inputString))

    def test_no_2(self):
        inputString = '   -42'
        output = -42

        solution = Solution()
        self.assertEqual(output, solution.myAtoi(inputString))

    def test_no_3(self):
        inputString = '4193 with words'
        output = 4193

        solution = Solution()
        self.assertEqual(output, solution.myAtoi(inputString))

    def test_no_4(self):
        inputString = 'words and 987'
        output = 0

        solution = Solution()
        self.assertEqual(output, solution.myAtoi(inputString))

    def test_no_5(self):
        inputString = "-91283472332"
        output = -2147483648

        solution = Solution()
        self.assertEqual(output, solution.myAtoi(inputString))

    def test_no_6(self):
        inputString = "3.14159"
        output = 3

        solution = Solution()
        self.assertEqual(output, solution.myAtoi(inputString))

    def test_no_7(self):
        inputString = "-+12"
        output = 0

        solution = Solution()
        self.assertEqual(output, solution.myAtoi(inputString))

    def test_no_8(self):
        inputString = "+"
        output = 0

        solution = Solution()
        self.assertEqual(output, solution.myAtoi(inputString))

    def test_no_9(self):
        inputString = "00000-42a1234"
        output = 0

        solution = Solution()
        self.assertEqual(output, solution.myAtoi(inputString))
        
    def test_no_10(self):
        inputString = "-   234"
        output = 0

        solution = Solution()
        self.assertEqual(output, solution.myAtoi(inputString))

if __name__ == '__main__':
    unittest.main()