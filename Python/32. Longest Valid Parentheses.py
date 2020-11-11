"""Solution for problem #32. Longest Valid Parentheses

Description: Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring
"""

import unittest

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxLength = 0

        for k in range(2):
            left, right = 0, 0

            r = range(len(s)) if k == 0 else range(len(s) - 1, -1, -1) 

            for i in r:
                if s[i] == '(':
                    left += 1
                else:
                    right += 1

                if left == right:
                    if maxLength < right + left:
                        maxLength = right + left

                if (k == 0 and right > left) or (k == 1 and right < left):
                    left, right = 0, 0  

        return maxLength

class TestsForSolution(unittest.TestCase):
    def test_no_1(self):
        s = "(()"
        output = 2

        solution = Solution()
        self.assertEqual(output, solution.longestValidParentheses(s))

    def test_no_2(self):
        s = ")()())"
        output = 4

        solution = Solution()
        self.assertEqual(output, solution.longestValidParentheses(s))

    def test_no_3(self):
        s = ""
        output = 0

        solution = Solution()
        self.assertEqual(output, solution.longestValidParentheses(s))

    def test_no_4(self):
        s = "()(()"
        output = 2

        solution = Solution()
        self.assertEqual(output, solution.longestValidParentheses(s))

    def test_no_5(self):
        s = "(())("
        output = 4

        solution = Solution()
        self.assertEqual(output, solution.longestValidParentheses(s))

if __name__ == '__main__':
    unittest.main()