"""Solution for problem #20 `Valid Parentheses`

Description: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
"""

import unittest

class Solution:
    def isValid(self, s: str) -> bool:

        open_brackets = {'(', '{', '['}

        lookip = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []

        for c in s:
            if c in open_brackets:
                stack.append(c)
            elif stack:
                prev_bracket = stack.pop()

                if c != lookip[prev_bracket]:
                    return False
            else:
                return False

        return not stack

class TestsForSolution(unittest.TestCase):
    def test_no_1(self):
        input = "()"
        output = True

        solution = Solution()
        self.assertEqual(output, solution.isValid(input))

    def test_no_2(self):
        input = "()[]{}"
        output = True

        solution = Solution()
        self.assertEqual(output, solution.isValid(input))

    def test_no_3(self):
        input = "(]"
        output = False

        solution = Solution()
        self.assertEqual(output, solution.isValid(input))

    def test_no_4(self):
        input = "([)]"
        output = False

        solution = Solution()
        self.assertEqual(output, solution.isValid(input))

    def test_no_5(self):
        input = "{[]}"
        output = True

        solution = Solution()
        self.assertEqual(output, solution.isValid(input))

    def test_no_6(self):
        input = "["
        output = False

        solution = Solution()
        self.assertEqual(output, solution.isValid(input))

    def test_no_7(self):
        input = "]"
        output = False

        solution = Solution()
        self.assertEqual(output, solution.isValid(input))         

if __name__ == '__main__':
    unittest.main()
