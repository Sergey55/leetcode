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
        # Obviosly all negative numbers not a palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        originalNumber = x
        revertNumber = 0

        while revertNumber < originalNumber:
            revertNumber = revertNumber * 10 + originalNumber % 10
            originalNumber //= 10

        print(revertNumber, originalNumber)

        return (revertNumber == originalNumber) or ((revertNumber // 10) == originalNumber)

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