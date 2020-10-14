# Solution for problem #9 `Palindrome Number`
#
# Description: Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
# Follow up: 
#   Could you solve it without converting the integer to a string?
#
# Score: 
#   Runtime: 56 ms, faster than 83.00% of Python3 online submissions for Palindrome Number.
#   Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Palindrome Number.

import unittest

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        tmp = x
        digits = []

        while tmp:
            digits.append(tmp % 10)
            tmp //= 10

        return digits == digits[::-1]

class TestsForSolution(unittest.TestCase):
    def test_no_1(self):
        input = 121
        output = True

        solution = Solution()
        self.assertEqual(output, solution.isPalindrome(input))

    def test_no_2(self):
        input = -121
        output = False

        solution = Solution()
        self.assertEqual(output, solution.isPalindrome(input))

    def test_no_3(self):
        input = 10
        output = False

        solution = Solution()
        self.assertEqual(output, solution.isPalindrome(input))

    def test_no_4(self):
        input = -101
        output = False

        solution = Solution()
        self.assertEqual(output, solution.isPalindrome(input))        

if __name__ == '__main__':
    unittest.main()