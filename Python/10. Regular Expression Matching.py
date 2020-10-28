"""Solution for problem #10 `Regular Expression Matching`

Description: Given an input string (s) and a pattern (p), 
implement regular expression matching with support for '.' and '*' where: 

    * '.' Matches any single character.​​​​
    * '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial)."""

import unittest

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        leftMatch = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return (leftMatch and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
        else:
            return leftMatch and self.isMatch(s[1:], p[1:])

        
class TestsForSolution(unittest.TestCase):

    def test_no_1(self):
        inputString = 'aa'
        pattern = 'a'
        output = False

        solution = Solution()
        self.assertEqual(output, solution.isMatch(inputString, pattern))

    def test_no_2(self):
        inputString = 'aa'
        pattern = 'a*'
        output = True

        solution = Solution()
        self.assertEqual(output, solution.isMatch(inputString, pattern))

    def test_no_3(self):
        inputString = 'ab'
        pattern = '.*'
        output = True

        solution = Solution()
        self.assertEqual(output, solution.isMatch(inputString, pattern))

    def test_no_4(self):
        inputString = 'aab'
        pattern = 'c*a*b'
        output = True

        solution = Solution()
        self.assertEqual(output, solution.isMatch(inputString, pattern))

    def test_no_5(self):
        inputString = 'mississippi'
        pattern = 'mis*is*p*.'
        output = False

        solution = Solution()
        self.assertEqual(output, solution.isMatch(inputString, pattern))

    def test_no_6(self):
        inputString = 'aa'
        pattern = '*a'
        output = False

        solution = Solution()
        self.assertEqual(output, solution.isMatch(inputString, pattern))

    def test_no_7(self):
        inputString = 'aaa'
        pattern = 'a*a'
        output = True

        solution = Solution()
        self.assertEqual(output, solution.isMatch(inputString, pattern))        

        

if __name__ == '__main__':
    unittest.main()